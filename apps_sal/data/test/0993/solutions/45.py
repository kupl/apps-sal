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
    for a in A:
        A_sum.append((A_sum[-1] + a) % m)

    D = defaultdict(int)
    res = 0
    for i in range(n + 1):
        res += D.get(A_sum[i], 0)
        D[A_sum[i]] += 1
    print(res)


def __starting_point():
    resolve()

__starting_point()
