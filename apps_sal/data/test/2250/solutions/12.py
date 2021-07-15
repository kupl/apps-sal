def subsolve(a):
    n = len(a)
    dp = [[0] * 4 for _ in range(n + 1)]
    if a[0] == 'R':
        dp[0] = [0, n, n, n]
    else:
        dp[0] = [1, n, n, n]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][2], dp[i - 1][3]) + int(a[i] != 'R')
        dp[i][1] = min(dp[i - 1][0], n) + int(a[i] != 'R')
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + int(a[i] != 'L')
        dp[i][3] = min(dp[i - 1][2], n) + int(a[i] != 'L')
    return min(dp[n - 1][2], dp[n - 1][3], n)

def solve():
    n = int(input())
    a = input()
    a += a
    ans = n
    for i in range(min(n, 4)):
        ans = min(ans, subsolve(a[i:i + n]))
    print(ans)

t = int(input())
for _ in range(t):
    solve()
