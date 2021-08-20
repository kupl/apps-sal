import sys
inf = (1 << 31) - 1


def solve():
    (n, k) = map(int, input().split())
    if k > n - k:
        k = n - k
    bit = BinaryIndexedTree([0] * n)
    s = 0
    res = 1
    ans = []
    for i in range(n):
        t = (s + k) % n
        if s < t:
            res += bit.get_sum(t) - bit.get_sum(s + 1) + 1
            ans.append(res)
        else:
            res += bit.get_sum(n) - bit.get_sum(s + 1)
            res += bit.get_sum(t) + 1
            ans.append(res)
        bit.add(s, 1)
        bit.add(t, 1)
        s = t
    print(*ans)


class BinaryIndexedTree:
    """ 1-origin Binary Indexed Tree """

    def __init__(self, a):
        self.n = len(a)
        self.bit = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.bit[i] += a[i - 1]
            if i + (i & -i) <= self.n:
                self.bit[i + (i & -i)] += self.bit[i]

    def add(self, i, x):
        """ a_i += x """
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def get_sum(self, r):
        """ sum(a[0 .. r)) """
        res = 0
        while r > 0:
            res += self.bit[r]
            r -= r & -r
        return res


def __starting_point():
    solve()


__starting_point()
