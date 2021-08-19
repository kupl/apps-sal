import itertools
N, K = [int(_) for _ in input().split()]
P = [int(_) - 1 for _ in input().split()]
C = [int(_) for _ in input().split()]


class SegmentTree():
    def __init__(self, array, f, ti):
        """
        Parameters
        ----------
        array : list
            to construct segment tree from
        f : func
            binary operation of the monoid
        ti : 
            identity element of the monoid
        """
        self.f = f
        self.ti = ti
        self.n = n = 2**(len(array).bit_length())
        self.dat = dat = [ti] * n + array + [ti] * (n - len(array))
        for i in range(n - 1, 0, -1):  # build
            dat[i] = f(dat[i << 1], dat[i << 1 | 1])

    def update(self, p, v):  # set value at position p (0-indexed)
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = v
        while p > 1:
            p >>= 1
            dat[p] = f(dat[p << 1], dat[p << 1 | 1])

    def operate_right(self, p, v):  # apply operator from the right side
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = f(dat[p], v)
        while p > 1:
            p >>= 1
            dat[p] = f(dat[p << 1], dat[p << 1 | 1])

    def operate_left(self, p, v):  # apply operator from the left side
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = f(v, dat[p])
        while p > 1:
            p >>= 1
            dat[p] = f(dat[p << 1], dat[p << 1 | 1])

    def query(self, l, r):  # result on interval [l, r) (0-indexed)
        f, ti, n, dat = self.f, self.ti, self.n, self.dat
        vl = vr = ti
        l += n
        r += n
        while l < r:
            if l & 1:
                vl = f(vl, dat[l])
                l += 1
            if r & 1:
                r -= 1
                vr = f(dat[r], vr)
            l >>= 1
            r >>= 1
        return f(vl, vr)


ans = -10**20
se = set()
for start in range(N):
    if start in se:
        continue
    now = start
    scores = []
    while True:
        if now in se:
            break
        se.add(now)
        scores += [C[now]]
        now = P[now]
    cyclelen = len(scores)
    cum = list(itertools.accumulate(scores * 2))
    st = SegmentTree(cum, max, -10**20)
    cycle, residue = divmod(K, cyclelen)
    ans = max([ans] + [
        st.query(start2 + 1, start2 + 1 + min(cyclelen, K)) - cum[start2]
        for start2 in range(cyclelen)
    ])
    if cum[-1] > 0 and cycle > 0:
        v1 = cum[-1] * (cycle - 1) // 2 + max(
            st.query(start2, start2 + cyclelen + 1) - cum[start2]
            for start2 in range(cyclelen))
        v2 = cum[-1] * cycle // 2 + max(
            st.query(start2, start2 + residue + 1) - cum[start2]
            for start2 in range(cyclelen))
        ans = max([ans, v1, v2])
print(ans)
