import heapq
N, C, *STC = [int(_) for _ in open(0).read().split()]
STC = [(s, t, c) for s, t, c in zip(STC[::3], STC[1::3], STC[2::3])]
STC.sort()
#もしcを映しているテレビがあるならこれにしてしまうのが最適
#cを映しているテレビがないならすでに終わっているテレビのどれかを選ぶ
#どのテレビもすでに映しているなら新しいテレビを追加する

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

ti = (10 ** 10, -10 ** 10)
st = SegmentTree([(10 ** 10, i) for i in range(C + 1)], min, ti)
ans = 0
for s, t, c in STC:
    if st.query(c, c + 1)[0] == 10 ** 10:
        t2, c2 = st.query(1, C + 1)
        if t2 < s:
            st.update(c2, (10 ** 10, c2))
        else:
            ans += 1
    st.update(c, (t, c))
print(ans)

