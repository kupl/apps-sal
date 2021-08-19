import math
(a, b) = list(map(int, input().split()))
d = a
cnt_2 = 0
cnt_5 = 0
while a % 2 == 0:
    a /= 2
    cnt_2 += 1
while a % 5 == 0:
    a /= 5
    cnt_5 += 1
umn = 1
cnt_2_raz = max(b - cnt_2, 0)
cnt_5_raz = max(b - cnt_5, 0)
while cnt_2_raz > 0:
    umn *= 2
    cnt_2_raz -= 1
while cnt_5_raz > 0:
    umn *= 5
    cnt_5_raz -= 1
print(d * umn)
