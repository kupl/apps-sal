# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
A = list(map(int,input().split()))

# 各数字に必要なマッチの本数
num = [0,2,5,5,4,5,6,3,7,6]

# dp : i本のマッチで作ることが可能な最大の桁数
dp = [-float("inf")]*(N+1)
# dp初期化 
#   - 0本 -> 0桁
#   - 各数字を1つ作る場合は1桁
dp[0] = 0
for a in A:
    if num[a] <= N:
        dp[num[a]] = 1

# dp更新
for i in range(1,N+1):
    for a in A:
        if i - num[a] >= 0:
            dp[i] = max(dp[i], dp[i-num[a]] + 1)

# 復元
A.sort(reverse=True)
ans = ""
for i in range(dp[N]):
    for a in A:
        if N-num[a] >= 0 and dp[N-num[a]] == dp[N]-1:
            ans += str(a)
            N -= num[a]
            break

print(ans)
