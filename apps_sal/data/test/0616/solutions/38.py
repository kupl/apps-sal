n, m = map(int, input().split())

abcsl = []
for _ in range(m):
    a, b = map(int, input().split())
    cl = list(map(int, input().split()))
    abcsl.append((a, b, cl))

dp = [10**9] * (2**n)
dp[0] = 0
for a, b, cl in abcsl:
    b_bit = 0
    for c in cl:
        b_bit += 2**(c - 1)
    for i in range(2**n):
        dp[i | b_bit] = min(dp[i] + a, dp[i | b_bit])

if dp[2**n - 1] == 10**9:
    print(-1)
else:
    print(dp[2**n - 1])
