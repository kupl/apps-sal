import sys
from itertools import accumulate
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))

    R = [0] + list(accumulate(A))
    R_mod = [r % m for r in R]

    D = Counter(R_mod)
    res = 0
    for v in list(D.values()):
        res += (v - 1) * v // 2
    print(res)


def __starting_point():
    resolve()


__starting_point()
