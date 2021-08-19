from math import gcd


class SegmentTree:

    def __init__(self, list, f=lambda x, y: x + y, inf=0):
        self.height = (len(list) - 1).bit_length() + 1
        self.zero = 2 ** (self.height - 1)
        self.id = inf
        self.tree = [self.id] * 2 ** self.height
        self.f = f
        for i in range(len(list)):
            self.tree[self.zero + i] = list[i]
        for i in range(self.zero - 1, 0, -1):
            self.tree[i] = self.f(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, x):
        i += self.zero
        self.tree[i] = x
        while i > 1:
            i //= 2
            self.tree[i] = self.f(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        l += self.zero
        r += self.zero
        (lf, rf) = (self.id, self.id)
        while l < r:
            if l & 1:
                lf = self.f(lf, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                rf = self.f(self.tree[r], rf)
            l //= 2
            r //= 2
        return self.f(lf, rf)
    '\n    FFFFTTTTとしたときの最小のTを求める\n    '

    def BinarySearch(self, l, r, f):
        if not f(self.query(l, r)):
            return r
        l += self.zero
        while True:
            if f(self.tree[l]):
                if l >= self.zero:
                    return l - self.zero + 1
                else:
                    l *= 2
            elif l % 2 == 0:
                l += 1
            else:
                l = l // 2 + 1


n = int(input())
a = list(map(int, input().split()))
S = SegmentTree(a, gcd)
ans = 0
for i in range(n):
    S.update(i, 0)
    ans = max(ans, S.tree[1])
    S.update(i, a[i])
print(ans)
