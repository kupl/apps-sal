# -*- coding: utf-8 -*-
# 標準入力を取得
A, B = list(map(int, input().split()))

# 求解処理
ans = str()
if (A <= 8) and (B <= 8):
    ans = "Yay!"
else:
    ans = ":("

# 結果出力
print(ans)
