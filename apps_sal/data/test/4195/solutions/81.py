# -*- coding: utf-8 -*-
# 標準入力を取得
D, N = list(map(int, input().split()))

# 求解処理
ans = (N + (N // 100)) * 100**D

# 結果出力
print(ans)
