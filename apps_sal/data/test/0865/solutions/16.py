import sys
input = sys.stdin.readline


def solve():
    N, T = list(map(int, input().split()))
    items = [tuple(map(int, input().split())) for _ in range(N)]

    items.sort()

    capW = T - 1
    dp = [0] * (capW + 1)
    ans = 0
    for wi, vi in items:
        ans = max(ans, dp[-1] + vi)
        for w in reversed(list(range(wi, capW + 1))):
            v0 = dp[w - wi] + vi
            if v0 > dp[w]:
                dp[w] = v0

    print(ans)


solve()
