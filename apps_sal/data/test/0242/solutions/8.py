from math import *
n = int(input())
per = 0
per2 = 5
cou = 0
cou2 = 1
while per < n:
    cou2 += 1
    while per2 % 5 == 0:
        per2 = per2 // 5
        per += 1
    if per == n:
        cou = 1
        per2 = (cou2 - 1) * 5
        break
    per2 = cou2 * 5
if cou == 1:
    print(5)
    print(per2, per2 + 1, per2 + 2, per2 + 3, per2 + 4)
else:
    print(0)
