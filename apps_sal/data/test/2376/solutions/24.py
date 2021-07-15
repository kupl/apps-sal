import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N, W = [int(x) for x in input().split()]
    WV = [[int(x) for x in input().split()] for _ in range(N)]

    weight = set()
    weight.add(0)
    weight.add(WV[0][0])
    for i in range(1, N + 1):
        for j in range(3 * i):
            weight.add(WV[0][0] * i + j)

    weight = sorted(list(weight))

    dp = defaultdict(int)

    for i in range(N):
        for j in weight[::-1]:
            if j >= WV[i][0]:
                dp[j] = max(dp[j], dp[j - WV[i][0]] + WV[i][1])

    ans = 0
    for i in weight:
        if i > W:
            break
        ans = max(ans, dp[i])

    print(ans)


def __starting_point():
    main()

__starting_point()
