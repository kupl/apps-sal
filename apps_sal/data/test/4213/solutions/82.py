# -*- coding: utf-8 -*-
# モジュールのインポート
import itertools

# 標準入力を取得
N = int(input())
A = list(map(int, input().split()))

# 求解処理
ans = 0
for A_i, A_j in itertools.combinations(A, r=2):
    ans = max(ans, abs(A_i - A_j))

# 結果出力
print(ans)
