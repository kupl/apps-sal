# -*- coding: utf-8 -*-

n = int(input())

count = 0
max_divisor_n = n // 2
for a in range(1, n):
    # ループは a >= b で回し、a != b の時は入れ替えたケースもカウントする
    for b in range(1, a+1):
        if a*b >= n:
            break
        # c = n - a*b とすればよい
        count += 1
        if a != b:
            count += 1
print(count)
