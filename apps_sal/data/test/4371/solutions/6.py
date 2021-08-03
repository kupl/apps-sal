# abc114b
# https://atcoder.jp/contests/abc114/tasks/abc114_b

# 数字1,2...9からなる文字列S
# Sから連続する3個の数字を取り出し、1つの整数Xとする

# Xと753の差（の絶対値）は最小でいくつになるか？
# ※並び替えは出来ない

# abs:絶対値もとめる関数
# min:最小値もとめる関数

# 入力
s = str(input())

# 処理
# Xと753の差の絶対値の格納
abs_list = []

for i in range(1, len(s) - 1):
    # Sのi番目から3つ順番に取得
    x = int(s[i - 1: i + 2])
    # 753との差
    abs_list.append(abs(x - 753))

# リストに入れたものの最小値
answer = min(abs_list)
print(answer)
