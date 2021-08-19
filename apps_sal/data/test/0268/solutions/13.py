import bisect
import sys
input = sys.stdin.readline


class SegmentTree:

    def __init__(self, n, op, e):
        self.n = n
        self.op = op
        self.e = e
        self.size = 2 ** (n - 1).bit_length()
        self.node = [self.e] * (2 * self.size)

    def built(self, array):
        for i in range(self.n):
            self.node[self.size + i] = array[i]
        for i in range(self.size - 1, 0, -1):
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def update(self, i, val):
        i += self.size
        self.node[i] = val
        while i > 1:
            i >>= 1
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def get_val(self, l, r):
        (l, r) = (l + self.size, r + self.size)
        (res_l, res_r) = (self.e, self.e)
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.node[r], res_r)
            (l, r) = (l >> 1, r >> 1)
        return self.op(res_l, res_r)


(n, k, d) = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
st = SegmentTree(n + 1, lambda a, b: a | b, 0)
st.update(0, 1)
for i in range(n):
    tmp = bisect.bisect_left(a, a[i] - d)
    if tmp >= max(i + 2 - k, 0):
        continue
    st.update(i + 1, st.get_val(tmp, max(i + 2 - k, 0)))
if st.get_val(n, n + 1) == 1:
    print('YES')
else:
    print('NO')
