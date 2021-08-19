# a, bを数値型として取得する
vals = list(map(int, input().split()))

# 昇順にソートして各値を取得
min_val, max_val = sorted(vals)

# 小さい値の方をもう一方の値の分だけ繰り返し文字列結合させる
ret = str(min_val) * max_val

# 結果を表示
print(ret)
