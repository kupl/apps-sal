# -*- coding: utf-8 -*-
# 標準入力を取得
R = int(input())

# 求解処理
ans = str()
if R < 1200:
    ans = "ABC"
elif R < 2800:
    ans = "ARC"
else:
    ans = "AGC"

# 結果出力
print(ans)
