from math import gcd
N = int(input())
A = list(map(int, input().split()))


class SegmentTree(object):

    def __init__(self, init_val, segfunc, ide_ele):
        self.init_val = init_val
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        n = len(init_val)
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res

    def update(self, k, val):
        k += self.num
        self.tree[k] = val
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1


def segfunc(x, y):
    return gcd(x, y)


def get_lcm(a, b):
    return a * b // gcd(a, b)


g = A[0]
for a in A[1:]:
    g = get_lcm(g, a)
ide_ele = g
st = SegmentTree(A, segfunc, ide_ele)
res = 0
for i in range(N):
    left = st.query(0, i)
    right = st.query(i + 1, N)
    res = max(res, gcd(left, right))
print(res)
