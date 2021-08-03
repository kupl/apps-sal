# 入力を受ける
import itertools
N = int(input())
d = list(map(int, input().split()))

# dから2個選び、総和をとる
rec = 0
for tako in itertools.combinations(d, 2):
    rec += tako[0] * tako[1]
print(rec)
