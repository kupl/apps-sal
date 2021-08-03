from sys import stdin
uu = 0
n = int(stdin.readline().strip())
s1 = stdin.readline().strip()
s = list(map(int, stdin.readline().strip().split()))
dp = [-1 for i in range(n + 1)]


def sol1(x):
    if dp[x] != -1:
        return dp[x]
    if x == 0:
        return 0
    ans = 0
    for i in range(x):
        ans = max(ans, s[i] + sol1(x - i - 1))
    dp[x] = ans


for i in range(n):
    sol1(i + 1)
dp[0] = 0
s2 = []
x = 1
for i in range(1, len(s)):
    if s1[i] != s1[i - 1]:
        s2.append(x)
        x = 1
    else:
        x += 1
s2.append(x)
dp1 = [[[-1 for i in range(n + 1)]for j in range(n + 1)] for k in range(n + 1)]
n = len(s2)
s = s2.copy()


def sol(l, r, k):
    if l == r:
        return dp[s[l] + k]
    if l > r:
        return 0
    if dp1[l][r][k] != -1:
        return dp1[l][r][k]

    ans = 0
    for i in range(l, r + 1, 2):
        if i != l:
            ans = max(ans, sol(l + 1, i - 1, 0) + sol(i, r, s[l] + k))
        else:
            ans = max(ans, sol(i + 1, r, 0) + dp[s[l] + k])

    dp1[l][r][k] = ans
    return ans


print(sol(0, len(s) - 1, 0))
