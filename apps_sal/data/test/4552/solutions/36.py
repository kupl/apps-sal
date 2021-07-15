import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    F = [list(map(int, input().split())) for _ in range(n)]
    P = [list(map(int, input().split())) for _ in range(n)]

    res = -f_inf
    for pattern in product([0, 1], repeat=10):
        if sum(pattern) == 0:
            continue
        tmp = 0
        for i in range(n):
            cnt = 0
            for p, f in zip(pattern, F[i]):
                if p == 1 and f == 1:
                    cnt += 1
            tmp += P[i][cnt]
        res = max(res, tmp)
    print(res)


def __starting_point():
    resolve()

__starting_point()
