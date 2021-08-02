# -*- coding: utf-8 -*-
import sys
import itertools

# 標準入力を取得
A = list(map(int, input().split()))

# 求解処理
ans = sys.maxsize
for A_1, A_2, A_3 in itertools.permutations(A, r=3):
    ans = min(ans, abs(A_2 - A_1) + abs(A_3 - A_2))

# 結果出力
print(ans)
