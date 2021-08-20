import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


S = sr()[::-1]
MOD = 10 ** 9 + 7
answer = 0
dp = [0, 0, 1]
for i in range(len(S)):
    s = S[i]
    if s == 'A':
        answer += dp[1]
    elif s == 'B':
        dp[1] += dp[0]
    elif s == 'C':
        dp[0] += dp[2]
    elif s == '?':
        answer *= 3
        answer += dp[1]
        dp[1] *= 3
        dp[1] += dp[0]
        dp[0] *= 3
        dp[0] += dp[2]
        dp[2] *= 3
    answer %= MOD
    dp[0] %= MOD
    dp[1] %= MOD
    dp[2] %= MOD
print(answer)
