import sys
from itertools import product
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, A, B, C) = list(map(int, input().split()))
    goal = [A, B, C]
    L = list((int(input()) for _ in range(n)))
    res = f_inf
    for pattern in product([0, 1, 2, 3], repeat=n):
        cnt = [0] * 3
        length = [0] * 3
        for (idx, p) in enumerate(pattern):
            if p != 0:
                length[p - 1] += L[idx]
                cnt[p - 1] += 1
        mp = 0
        for i in range(3):
            if cnt[i] == 0:
                break
            mp += abs(goal[i] - length[i]) + (cnt[i] - 1) * 10
        else:
            res = min(res, mp)
    print(res)


def __starting_point():
    resolve()


__starting_point()
