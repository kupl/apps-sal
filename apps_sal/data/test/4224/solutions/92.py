# -*- coding: utf-8 -*-
# 標準入力を取得
N = int(input())
a = list(map(int, input().split()))

# 求解処理


def get_divisible_count(x: int) -> int:
    divisible_count = 0
    while x % 2 == 0:
        divisible_count += 1
        x /= 2
    return divisible_count


ans = 0
for n in range(N):
    ans += get_divisible_count(a[n])

# 結果出力
print(ans)
