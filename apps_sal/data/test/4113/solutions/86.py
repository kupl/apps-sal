# -*- coding: utf-8 -*-
# 標準入力を取得
N = int(input())

# 求解処理
ans = "No"
for d in range(N // 7 + 1):
    if (N - 7 * d) % 4 == 0:
        ans = "Yes"
        break

# 結果出力
print(ans)

