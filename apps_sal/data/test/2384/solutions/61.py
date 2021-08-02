from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
# n=2*pow(10,5)
# a=range(1,pow(10,5)+1)
# dp[i][j]:i番目の数字の中からj個数字を取った時の最大。(i//2)-1<=j<=(i+1)//2
# 求めるのはdp[n][n//2]
dp = defaultdict(lambda: -pow(10, 18))
dp[(1, 1)] = a[0]
for i in range(2, n + 1):  # i番目の数字はa[i-1]
    for j in range(i // 2 - 1, (i + 1) // 2 + 1):
        if j == 1:
            dp[(i, j)] = max(dp[(i - 1, 1)], a[i - 1])
        elif j == 0:
            dp[(i, j)] = 0
        else:
            dp[(i, j)] = max(dp[(i - 2, j - 1)] + a[i - 1], dp[(i - 1, j)])
print(dp[(n, n // 2)])
