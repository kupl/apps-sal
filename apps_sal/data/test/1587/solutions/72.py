# Nとcの定義
N = int(input())
C = input()

# 赤色の個数
red_num = str.count(C, "R")

# 左からred_num個までに含まれる白色の個数
white_num_left = str.count(C[:red_num], "W")

# 最小の操作回数
min_ope = white_num_left

# 最小の操作回数の出力
print(min_ope)
