# -*- coding: utf-8 -*-
# 標準入力を取得
N = int(input())

# 求解処理


def S(n: int) -> int:
    return sum(map(int, str(n)))


ans = str()
if N % S(N) == 0:
    ans = "Yes"
else:
    ans = "No"

# 結果出力
print(ans)
