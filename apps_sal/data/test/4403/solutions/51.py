# -*- coding: utf-8 -*-
# 標準入力を取得
S = input()

# 求解処理
ans = S.count("+") - S.count("-")

# 結果出力
print(ans)
