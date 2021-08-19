import sys
from itertools import product
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, m) = list(map(int, input().split()))
    XYZ = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for (x, y, z) in product([-1, 1], repeat=3):
        total = []
        for (X, Y, Z) in XYZ:
            s = X * x + Y * y + Z * z
            total.append(s)
        total.sort(reverse=True)
        res = max(res, sum(total[:m]))
    print(res)


def __starting_point():
    resolve()


__starting_point()
