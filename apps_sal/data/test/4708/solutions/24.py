# 数値の取得
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# 宿泊費の計算後結果を出力
if N <= K:
    account = N * X
else:
    account = (K * X) + (max(N - K, 0) * Y)

print(account)
