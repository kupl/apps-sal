n, L = [int(k) for k in input().split(' ') if k]
dp = [int(k) for k in input().split(' ') if k]
for i in range(1, n):
    dp[i] = min(2 * dp[i - 1], dp[i])
binary = []
while L != 0:
    binary.append(L % 2)
    L //= 2
while len(dp) < len(binary):
    dp.append(2 * dp[-1])


def minify(p):
    result = 999999999999999999999999999
    for i in range(p + 1, len(dp)):
        result = min(result, dp[i])
    if p == 0:
        return min(result, (dp[p] if binary[p] else 0))
    return min(result, (dp[p] if binary[p] else 0) + minify(p - 1))


print(minify(len(binary) - 1))
