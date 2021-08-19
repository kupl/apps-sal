import sys
from collections import Counter
NUM = int(1000000000.0 + 7)


def compute1(size, tots):
    val = 0
    ans = 0
    for i in range(tots):
        delic = val + 1
        ans += delic
        val = (val % NUM + delic % NUM) % NUM
    print('=--')
    for i in range(size - tots):
        delic = val
        ans += delic
        val = (val % NUM + delic % NUM) % NUM
        print(delic)
    print('=--')
    return ans % int(1000000000.0 + 7)


def compute2(size, tots):
    ans = power(2, tots, NUM) - 1
    ans = ans % NUM * power(2, size - tots, NUM) % NUM
    return ans


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


def solution(n, q, arr):
    st = SegmentTree(arr, '+')
    for x in range(q):
        (l, r) = [int(val) for val in sys.stdin.readline().split()]
        l -= 1
        r -= 1
        size = r - l + 1
        tots = st.query(l, r)
        print(compute2(size, tots))


def validate():
    from random import randint
    for i in range(1, 20000):
        tots = randint(0, i)
        val1 = compute1(i, tots)
        val2 = compute2(i, tots)
        if val1 != val2:
            print(val1, val2)
            raise Exception()


def random_query(n):
    from random import randint
    l = randint(0, n - 1)
    r = randint(0, n - 1)
    while r < l:
        r = randint(0, n - 1)
    return (l, r)


def random_sequence(n):
    from random import randint
    return [randint(0, 1) for val in range(n)]


class SegmentTree(object):

    def __init__(self, data, op):
        from math import log
        from math import ceil
        self.n = len(data)
        self.tree = [0] * self.n * 4
        self.merge_op = op
        self._build_tree(data, 0, 0, self.n - 1)

    def _build_tree(self, data, ind, lo, hi):
        if lo == hi:
            self.tree[ind] = data[lo]
            return
        mid = lo + (hi - lo) // 2
        self._build_tree(data, 2 * ind + 1, lo, mid)
        self._build_tree(data, 2 * ind + 2, mid + 1, hi)
        self.tree[ind] = self._merge(self.tree[2 * ind + 1], self.tree[2 * ind + 2])

    def _merge(self, val1, val2):
        if self.merge_op == '+':
            return val1 + val2
        elif self.merge_op == 'OR':
            return val1 | val2
        elif self.merge_op == 'XOR':
            return val1 ^ val2
        elif self.merge_op == '*':
            return val1 * val2

    def query(self, i, j, ind=0, lo=0, hi=None):
        if hi == None:
            hi = self.n - 1
        if lo > j or hi < i:
            raise Exception()
            return 0
        if i <= lo and j >= hi:
            return self.tree[ind]
        mid = lo + (hi - lo) // 2
        if i > mid:
            return self.query(i, j, 2 * ind + 2, mid + 1, hi)
        elif j <= mid:
            return self.query(i, j, 2 * ind + 1, lo, mid)
        lq = self.query(i, mid, 2 * ind + 1, lo, mid)
        rq = self.query(mid + 1, j, 2 * ind + 2, mid + 1, hi)
        return self._merge(lq, rq)


def __starting_point():
    (n, q) = [int(val) for val in sys.stdin.readline().split()]
    arr = [int(val) for val in sys.stdin.readline().split()[0]]
    solution(n, q, arr)


__starting_point()
