import sys

L = list(sys.stdin.readline().strip())
mod = 10**9 + 7
ls = len(L)

# 左からi桁目で、L以下が確定しているかどうか（True /False）の場合の(a, b)の組み合わせの総数
dp = [[0 for i in (True, False)] for _ in range(ls)]
# 1からしか始まらない
dp[0][False] = 2
dp[0][True] = 1
 
for i in range(ls-1):
    for j in (True, False):
        if L[i+1] == "1":
            dp[i+1][True] = 3 * dp[i][True] + 1 * dp[i][False]
            dp[i+1][False] = 2 * dp[i][False]
        else:
            dp[i+1][True] = 3 * dp[i][True]
            # dp[i+1][False] = 1 * dp[i][False]
            dp[i+1][False] = 1 * dp[i][False]
        dp[i+1][True] %= mod
        dp[i+1][False] %= mod
 
print(sum(dp[ls-1]) % mod)
