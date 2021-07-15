import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    XYZ = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for pattern in product([0, 1], repeat=3):
        op = [1 if p == 0 else -1 for p in pattern]
        tmp = [0] * n
        for i in range(n):
            tmp[i] = sum([o * num for o, num in zip(op, XYZ[i])])
        tmp.sort(reverse=True)
        res = max(res, sum(tmp[:m]))
    print(res)


def __starting_point():
    resolve()

__starting_point()
