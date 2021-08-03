n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[[False for i in range(101)] for j in range(101)] for k in range(101)]


def f(i, j, k):
    if not dp[i][j][k]:
        if i == j:
            dp[i][j][k] = 0
        else:
            dp[i][j][k] = f(i + 1, j, 0) + a[k]
            for m in range(i + 1, j):
                if s[i] == s[m]:
                    dp[i][j][k] = max(dp[i][j][k], f(i + 1, m, 0) + f(m, j, k + 1))
    return dp[i][j][k]


answer = f(0, n, 0)
print(answer)
