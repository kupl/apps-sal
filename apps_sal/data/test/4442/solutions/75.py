# a, bを数値型として取得する
vals = list(map(int, input().split()))

# 小さい値の方を判定
min_val, max_val = sorted(vals)

# 小さい値の方をもう一方の値の分だけ繰り返し文字列結合させる
ret = ''
for i in range(max_val):
    ret += str(min_val)

# 結果を表示
print(ret)
