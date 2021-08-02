# -*- coding: utf-8 -*-
# 標準入力を取得
A = list(map(int, input().split()))

# 求解処理
ans = max(A) - min(A)

# 結果出力
print(ans)
