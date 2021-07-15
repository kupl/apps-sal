n, m = map(int, input().split())
s = [input() for i in range(0, n)]
dp = [[n*m + 1] * 8 for i in range(0, n + 1)]


def minLenA(s):
    for i in range(0, len(s)):
        if '0' <= s[i] <= '9':
            return i;
    return m + 1

def minLenB(s):
    for i in range(0, len(s)):
        if 'a' <= s[i] <= 'z':
            return i;
    return m + 1

def minLenC(s):
    for i in range(0, len(s)):
        if s[i] in ["#", "*", "&"]:
            return i;
    return m + 1

dp[0][0] = 0
dp[0][1:] = [n*m + 1] * 7

l = [[0] * 3 for i in range(0, n)]
for i in range(0, n):
    l[i][0] = min(minLenA(s[i]),1 + minLenA(list(reversed(s[i]))))
    l[i][1] = min(minLenB(s[i]), 1 +minLenB(list(reversed(s[i]))))
    l[i][2] = min(minLenC(s[i]), 1 + minLenC(list(reversed(s[i]))))
for i in range(1, n + 1):
    for j in range(0, 8):
        dp[i][j] = min(dp[i - 1][j ^ 1] + l[i-1][0], dp[i-1][j],dp[i][j]);
        dp[i][j] = min(dp[i - 1][j ^ 2] + l[i-1][1], dp[i-1][j],dp[i][j]);
        dp[i][j] = min(dp[i - 1][j ^ 4] + l[i-1][2],dp[i-1][j],dp[i][j]);
print(dp[-1][7])
