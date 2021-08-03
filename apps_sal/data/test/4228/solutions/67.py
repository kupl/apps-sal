# N, Lを取得する
N, L = map(int, input().split())

# 味の総和を求める
La = N * L + (N - 1) * N / 2

# Le=（リンゴiを取り除いた時の味の総和）とLa=（全リンゴの味の総和）の絶対値が最小となる時のLeを求める
min_Le = La
abs_L = int(1e100)
for i in range(N):
    Li = L + (i + 1) - 1
    if abs((La - Li) - La) < abs_L:
        Le = La - Li
        abs_L = abs(Le - La)

# 結果出力
print(int(Le))
