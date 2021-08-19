from typing import Callable, List, Union
T = Union[int, str]


class SegmentTree:
    """Segment Tree"""
    __slots__ = ['e', 'op', '_n', '_size', 'tree']

    def __init__(self, a: List[T], e: T, op: Callable[[T, T], T]) -> None:
        self.e = e
        self.op = op
        self._n = len(a)
        self._size = 1 << (self._n - 1).bit_length()
        self.tree = [e] * self._size + a + [e] * (self._size - self._n)
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k: int) -> None:
        """Update the value of a[k]."""
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def set(self, k: int, x: T) -> None:
        """Assign x to a[k] in O(log n)."""
        assert 0 <= k < self._n
        k += self._size
        self.tree[k] = x
        while k:
            k >>= 1
            self._update(k)

    def get(self, k: int) -> T:
        """Return a[k] in O(1)."""
        assert 0 <= k < self._n
        return self.tree[k + self._size]

    def prod(self, l: int, r: int) -> T:
        """Return op(a[l], ..., a[r - 1]). Return e, if l == r.
        Complexity: O(log n)
        """
        assert 0 <= l <= r <= self._n
        (sml, smr) = (self.e, self.e)
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.tree[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def prod_all(self) -> T:
        """Return op(a[0], ..., a[n - 1]. Return e if n == 0.
        Complexity: O(1)
        """
        return self.tree[1]

    def max_right(self, l: int, f: Callable[[T], bool]) -> int:
        """
        Return an index r satisfying both:
            1. r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            2. r = n or f(op(a[l], a[l + 1], ..., a[r])) = false.

        If f is monotone, this is the maximum r satisfying:
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true.

        Complexity: O(log n)
        """
        assert 0 <= l <= self._n
        assert f(self.e)
        if l == self._n:
            return self._n
        l += self._size
        sm = self.e
        while True:
            while not l & 1:
                l >>= 1
            if not f(self.op(sm, self.tree[l])):
                while l < self._size:
                    l *= 2
                    if f(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self._size
            sm = self.op(sm, self.tree[l])
            l += 1
            if l & -l == l:
                break
        return self._n

    def min_left(self, r: int, f: Callable[[T], bool]) -> int:
        """
        Return an index l satisfying both:
            1. l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            2. l = 0 or f(op(a[l - 1], a[l + 1], ..., a[r - 1])) = false.
        If f is monotone, this is the minimum l satisfying:
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true.

        Complexity: O(log n)
        """
        assert 0 <= r <= self._n
        assert f(self.e)
        if not r:
            return 0
        r += self._size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not f(self.op(self.tree[r], sm)):
                while r < self._size:
                    r = 2 * r + 1
                    if f(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self._size
            if r & -r == r:
                break
        return 0


def practice2_j():
    (N, _, *AQ) = list(map(int, open(0).read().split()))
    (A, Q) = (AQ[:N], AQ[N:])
    tree = SegmentTree(A, -1, max)
    res = []
    for (t, x, y) in zip(*[iter(Q)] * 3):
        if t == 1:
            tree.set(x - 1, y)
        elif t == 2:
            res.append(tree.prod(x - 1, y))
        else:
            res.append(tree.max_right(x - 1, lambda n: n < y) + 1)
    print('\n'.join(map(str, res)))


def staticrmq():
    (N, Q, *ALR) = list(map(int, open(0).read().split()))
    (A, LR) = (ALR[:N], ALR[N:])
    tree = SegmentTree(A, 10 ** 10 + 1, min)
    res = [tree.prod(l, r) for (l, r) in zip(*[iter(LR)] * 2)]
    print('\n'.join(map(str, res)))


def dsl_2_a():
    (N, Q, *X) = list(map(int, open(0).read().split()))
    tree = SegmentTree([2 ** 31 - 1] * N, 2 ** 31 - 1, min)
    res = []
    for (com, x, y) in zip(*[iter(X)] * 3):
        if com:
            res.append(tree.prod(x, y + 1))
        else:
            tree.set(x, y)
    print('\n'.join(map(str, res)))


def abc125_c():
    from math import gcd
    (N, *A) = list(map(int, open(0).read().split()))
    tree = SegmentTree(A, 0, gcd)
    res = max((gcd(tree.prod(0, i), tree.prod(i + 1, N)) for i in range(N)))
    print(res)


def __starting_point():
    abc125_c()


__starting_point()
