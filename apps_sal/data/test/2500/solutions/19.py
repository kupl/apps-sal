import sys
p = 10 ** 9 + 7


def dthbit(d, n):
    return n >> d & 1


def main(n):
    dp = [[0 for _ in range(3)] for _ in range(64)]
    dp[63][0] = 1
    for d in range(62, -1, -1):
        b = dthbit(d, n)
        s = dp[d + 1][:]
        dp[d][0] = dp[d + 1][0] + (1 ^ b) * dp[d + 1][1] % p
        dp[d][1] = b * dp[d + 1][0] + dp[d + 1][1] % p
        dp[d][2] = (1 + b) * dp[d + 1][1] + 3 * dp[d + 1][2] % p
    return sum(dp[0][:]) % p


n = int(input())
print(main(n))
