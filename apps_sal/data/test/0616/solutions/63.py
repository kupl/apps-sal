import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    keys = []
    for _ in range(m):
        bit = ["0"] * n
        a, b = list(map(int, input().split()))
        C = list(map(int, input().split()))
        for c in C:
            bit[c - 1] = "1"
        bit = int("".join(bit), 2)
        keys.append([bit, a])

    dp = [f_inf] * (1 << n)
    dp[0] = 0
    for i in range(1 << n):
        for k, cost in keys:
            idx = i | k
            dp[idx] = min(dp[idx], dp[i] + cost)

    print((dp[-1] if dp[-1] != f_inf else -1))


def __starting_point():
    resolve()

__starting_point()
