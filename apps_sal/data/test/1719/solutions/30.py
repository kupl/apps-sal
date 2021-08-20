N = int(input())
mod = 10 ** 9 + 7
dp = [{} for i in range(N)]
list = ['AGC', 'ACG', 'GAC']


def dfs(x, y):
    if x in list:
        return 0
    if y == N:
        return 1
    if x in dp[y]:
        return dp[y][x]
    ans = 0
    for i in 'ACGT':
        if x[0] == 'A' and i == 'C' and (x[1] == 'G' or x[2] == 'G'):
            continue
        ans += dfs(x[1:] + i, y + 1)
    dp[y][x] = ans % mod
    return ans % mod


print(dfs('TTT', 0))
