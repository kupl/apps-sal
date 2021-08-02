import itertools as it
# 入力の整数K, S
K, S = map(int, input().split())


counter = 0
# 3つの変数を作る
for x in range(0, K + 1):
    for y in range(0, K + 1):
        if K >= (S - x - y) and (S - x - y) >= 0:
            counter += 1
print(counter)
