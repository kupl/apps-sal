
MAX_DIGIT = 40
SMALL = 0
EQUAL = 1
N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-1 for _ in range(2)] for _ in range(MAX_DIGIT + 1)]
dp[0][EQUAL] = 0

for d in range(MAX_DIGIT):
    shift = MAX_DIGIT - d - 1
    bit_count = 0
    for a in A:
        if a >> shift & 1:
            bit_count += 1

    cost0 = (1 << shift) * bit_count
    cost1 = (1 << shift) * (N - bit_count)

    # small -> small
    if dp[d][SMALL] != -1:
        dp[d + 1][SMALL] = max(dp[d + 1][SMALL], dp[d][SMALL] + max(cost0, cost1))

    # equal -> small
    if dp[d][EQUAL] != -1:
        if K >> shift & 1:
            dp[d + 1][SMALL] = max(dp[d + 1][SMALL], dp[d][EQUAL] + cost0)

    # equal -> equal
    if dp[d][EQUAL] != -1:
        if K >> shift & 1:
            dp[d + 1][EQUAL] = max(dp[d + 1][EQUAL], dp[d][EQUAL] + cost1)
        else:
            dp[d + 1][EQUAL] = max(dp[d + 1][EQUAL], dp[d][EQUAL] + cost0)

ans = max(dp[MAX_DIGIT][EQUAL], dp[MAX_DIGIT][SMALL])
print(ans)
