# abc044_a
# https://atcoder.jp/contests/abc044/tasks/abc044_a

# 最初のK泊までは、X円
# K＋1泊目以降は、Y円

# N泊連続で宿泊した際の宿泊費

# 入力
n = int(input())
k = int(input())
x = int(input())
y = int(input())

# 処理

# x円とy円
if n > k:
    answer = k * x + (n - k) * y
# x円のみ
else:
    answer = n * x

print(answer)

