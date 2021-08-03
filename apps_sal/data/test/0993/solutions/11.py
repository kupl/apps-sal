import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))

    A_sum = [0]
    D = defaultdict(int)
    D[A_sum[-1]] += 1
    for a in A:
        A_sum.append((A_sum[-1] + a) % m)
        D[A_sum[-1]] += 1

    res = 0
    for v in list(D.values()):
        res += v * (v - 1) // 2
    print(res)


def __starting_point():
    resolve()


__starting_point()
