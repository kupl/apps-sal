import bisect
import operator
import collections


class RAQ():
    
    def __init__(self, size):
        """初期化"""
        self.size = size
        self.sub = [0 for i in range(size + 1)]
        self.r = 0
        self.v = 0
    
    @classmethod
    def from_array(cls, a):
        st = cls(len(a))
        for i, x in enumerate(a):
            st.add(i, i+1, x)
        return st

    def add(self, a, b, value):
        """区間[a, b) に対する加算"""
        if a > b:
            raise ValueError("a must be less than equal b.")
        self.sub[a] += value
        self.sub[b] -= value

    def get(self, key):
        """値の取得"""
        if key < self.r - 1:
            self.r = 0
            self.v = 0
        for i in range(self.r, key):
            self.v += self.sub[i]
        self.r = key
        return self.v + self.sub[key]


def read():
    N, D, A = list(map(int, input().strip().split()))
    XH = list()
    for i in range(N):
        x, h = list(map(int, input().strip().split()))
        XH.append((x, h))
    return N, D, A, XH


def solve(N, D, A, XH):
    XH = sorted(XH)
    X = [x for x, h in XH]
    H = [h for x, h in XH]

    st = RAQ.from_array(H)

    ans = 0
    i = 0
    while i < N:
        x = XH[i][0]
        h = st.get(i)
        c = h // A + (h % A > 0)
        ans += c
        v = c * A
        lidx = bisect.bisect_left(X, x)
        ridx = bisect.bisect_left(X, x + 2 * D + 1)
        st.add(lidx, ridx, -v)
        m = -1
        i += 1
        while i < N:
            h = st.get(i)
            if h > 0:
                break
            i += 1
    return ans


def __starting_point():
    inputs = read()
    print(("%s" % solve(*inputs)))

__starting_point()
