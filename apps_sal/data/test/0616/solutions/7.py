import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    keys = []
    for _ in range(m):
        a, b = list(map(int, input().split()))
        C = list(map(int, input().split()))
        s = 0
        for c in C:
            s |= 1 << (c - 1)
        keys.append([a, s])

    dp = [f_inf] * (1 << n)
    dp[0] = 0
    for now in range(1 << n):
        for cost, key in keys:
            nxt = now | key
            dp[nxt] = min(dp[nxt], dp[now] + cost)
    print((dp[-1] if dp[-1] != f_inf else -1))


def __starting_point():
    resolve()

__starting_point()
