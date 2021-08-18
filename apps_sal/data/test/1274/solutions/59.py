import sys
from itertools import accumulate

input = sys.stdin.readline


class SegmentTree:
    """Segment Tree class.

    Args:
        N (int): Number of elements
        X (list[int]): List for initialization
        func (callable): Function for interval.
        init_v (int): Initial value that does not affect `func`.
            For example, specify INF when `func = min`.

    References:
        <https://en.wikipedia.org/wiki/Segment_tree>
    """

    def __init__(self, N, X, func, init_v):
        N_ = 1
        while N_ < N:
            N_ *= 2
        self.N = N_
        self.func = func
        self.init_v = init_v
        self.__build(X)

    def __build(self, X):
        self.node = [[self.init_v, -1] for _ in range(2 * self.N)]

        for i, x in enumerate(X, self.N):
            self.node[i] = [x, i - self.N + 1]

        for i in range(self.N - 1, 0, -1):
            self.node[i] = self.func(self.node[i << 1], self.node[i << 1 | 1])

    def update(self, i, x):
        """Update the i-th node value to x.

        Args:
            i (int): index (1-based index)
            x (int): udpate value
        """
        i += self.N - 1
        self.node[i][0] = x
        while i > 1:
            i >>= 1
            self.node[i] = self.func(self.node[i << 1], self.node[i << 1 | 1])

    def query(self, l, r):
        """Query for right half-open interval [l, r).

        Args:
            l (int): index (1-based index)
            r (int): index (1-based index)
        """
        dst_l = [self.init_v, -1]
        dst_r = [self.init_v, -1]
        l += self.N - 1
        r += self.N - 1
        while l < r:
            if l & 1:
                dst_l = self.func(dst_l, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                dst_r = self.func(self.node[r], dst_r)
            l >>= 1
            r >>= 1
        return self.func(dst_l, dst_r)


def func(a, b):
    return a if a[0] > b[0] else b


def main():
    N, M = list(map(int, input().split()))
    AB = [None] * N
    for i in range(N):
        AB[i] = tuple(map(int, input().split()))

    AB.sort(key=lambda x: x[0])
    B = [0] * N
    C = [0] * (1 + 10 ** 5)
    for i, (a, b) in enumerate(AB):
        B[i] = b
        C[a] += 1
    C = list(accumulate(C))

    st = SegmentTree(N, B, func, -1)
    ans = 0
    l = 1
    for r in C[1:M + 1]:
        if r == 0:
            continue
        x, i = st.query(l, r + 1)
        if x == -1:
            continue
        ans += x
        st.update(i, -1)

    print(ans)


def __starting_point():
    main()


__starting_point()
