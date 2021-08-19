# -*- coding: utf-8 -*-
# モジュールのインポート
import sys

# 標準入力を取得
N, M = list(map(int, input().split()))
cakes = []
for n in range(N):
    cake_n = list(map(int, input().split()))
    cakes.append(cake_n)

# 求解処理
ans = -sys.maxsize
element = 3
for bit in range(1 << element):
    sign = [1 for i in range(element)]
    for i in range(element):
        if bit & (1 << i):
            sign[i] *= -1
    cakes = sorted(cakes, key=lambda x: sum(
        [sign[i] * x[i] for i in range(element)]), reverse=True)

    indicator = [0 for i in range(element)]
    for cake in cakes[:M]:
        for i in range(element):
            indicator[i] += cake[i]

    ans = max(ans, sum(map(abs, indicator)))

# 結果出力
print(ans)
