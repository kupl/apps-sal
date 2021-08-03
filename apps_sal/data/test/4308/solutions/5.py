# -*- coding: utf-8 -*-
# 標準入力を取得
N, K = list(map(int, input().split()))

# 求解処理
ans = 0
if N % K != 0:
    ans = 1

# 結果出力
print(ans)
