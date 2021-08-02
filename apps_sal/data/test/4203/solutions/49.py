# -*- coding: utf-8 -*-
# 標準入力を取得
S = input()

# 求解処理
ans = "AC"
if S[0] != "A":
    ans = "WA"

if S[2:-1].count("C") != 1:
    ans = "WA"
else:
    index = 2 + S[2:-1].index("C")
    if not (S[1:index] + S[index + 1:]).islower():
        ans = "WA"

# 結果出力
print(ans)
