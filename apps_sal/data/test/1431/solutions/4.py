# 入力
n = int(input())
a = list(map(int, input().split()))
# dpテーブル dp[i-1]はi番目の箱に入っているボールの数
dp = [0 for i in range(n)]
# 初期条件
dp[n - 1] = a[n - 1]

for i in range(n, 0, -1):
    num = 0
    for j in range(i * 2, n + 1, i):
        num = num + dp[j - 1]
    if num % 2 == a[i - 1]:
        dp[i - 1] = 0
    else:
        dp[i - 1] = 1

print(dp.count(1))
for i in range(n):
    if dp[i] == 1:
        print(i + 1, end=" ")
