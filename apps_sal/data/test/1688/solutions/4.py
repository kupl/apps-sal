import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

class Binary_Indexed_Tree():
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i):
        return self.sum_range(i, i)

    def sum(self, i):
        ret = 0
        while i:
            ret += self.data[i]
            i &= i-1
        return ret

    def sum_range(self, l, r):
        return self.sum(r)-self.sum(l-1)

    def lower_bound(self, w):
        if w<=0:
            return 0
        i = 0
        k = 1<<(self.n.bit_length())
        while k:
            if i+k <= self.n and self.data[i+k] < w:
                w -= self.data[i+k]
                i += k
            k >>= 1
        return i+1

class RangeMinimumQuery:
    def __init__(self, n, func=min, inf=float("inf")):
        self.n0 = 2**(n-1).bit_length()
        self.op = func
        self.inf = inf
        self.data = [self.inf]*(2*self.n0)

    def construct(self, lis):
        for i, x in enumerate(lis):
            self.data[i+self.n0-1] = x
        for i in range(self.n0-2, -1, -1):
            self.data[i] = self.op(self.data[2*i+1], self.data[2*i+2])

    def query(self, l,r):
        l += self.n0
        r += self.n0
        res = self.inf
        while l < r:
            if r&1:
                r -= 1
                res = self.op(res, self.data[r-1])
            if l&1:
                res = self.op(res, self.data[l-1])
                l += 1
            l >>=1
            r >>=1
        return res

n = int(input())
a = list(map(int, input().split()))
a = [i*2 for i in a]
BIT = Binary_Indexed_Tree(2*n)
RMQ = RangeMinimumQuery(2*n)
RMQ.construct(a+a)

b = [[j,i] for i,j in enumerate(a)]
b.sort(reverse=True)
ans = [0]*n
for j, i in b:
    cnt = BIT.sum(2*n-i)
    tmp = float("inf")
    if cnt:
        p = 2*n-BIT.lower_bound(cnt)
        tmp = p-i + ans[p%n]
    BIT.add(2*n-i, 1)
    BIT.add(n-i, 1)
    left = i
    right = 2*n
    if RMQ.query(i, right) < j//2:
        while right-left>1:
            mid = (right+left)//2
            if RMQ.query(i, mid) < j//2:
                right = mid
            else:
                left = mid
        tmp = min(tmp, right-i-1)
    ans[i] = tmp
ans = [i if i!=float("inf") else -1 for i in ans]
print(*ans)

