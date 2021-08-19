# -*- coding: utf-8 -*-
# 標準入力を取得
N = int(input())

# 求解処理
ans = N
if ans % 2 != 0:
    ans *= 2

# 結果出力
print(ans)
