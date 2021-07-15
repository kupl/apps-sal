import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    A, C = [], []
    for _ in range(m):
        a, b = list(map(int, input().split()))
        A.append(a)
        key = 0
        for c in map(int, input().split()):
            key |= 1 << (c - 1)
        C.append(key)

    dp = [f_inf] * (1 << n)
    dp[0] = 0
    for S in range(1 << n):
        for i in range(m):
            key, cost = C[i], A[i]
            dp[S | key] = min(dp[S | key], dp[S] + cost)
    print((dp[-1] if dp[-1] != f_inf else -1))


def __starting_point():
    resolve()

__starting_point()
