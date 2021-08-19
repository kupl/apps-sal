# -*- coding: utf-8 -*-
# 標準入力を取得
S = input()
T = input()

# 求解処理
N = len(S)
ans = "No"
for i in range(N):
    if S[-i:] + S[:-i] == T:
        ans = "Yes"
        break

# 結果出力
print(ans)
