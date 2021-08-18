import math
import sys
a = list(map(int, input().split()))
b = list(input())
if a[1] == a[3] and a[2] == a[4]:
    print(0)
    return
flag = False
c = 0
for i in range(len(b)):
    c += 1
    if b[i] == 'S':
        if math.fabs(a[4] - (a[2] - 1)) > math.fabs(a[4] - (a[2])):
            continue
        a[2] -= 1
    if b[i] == 'E':
        if math.fabs(a[3] - (a[1] + 1)) > math.fabs(a[3] - (a[1])):
            continue
        a[1] += 1
    if b[i] == 'W':
        if math.fabs(a[3] - (a[1] - 1)) > math.fabs(a[3] - (a[1])):
            continue
        a[1] -= 1
    if b[i] == 'N':
        if math.fabs(a[4] - (a[2] + 1)) > math.fabs(a[4] - (a[2])):
            continue
        a[2] += 1
    if a[1] == a[3] and a[2] == a[4]:
        flag = True
        break


if flag:
    print(c)
else:
    print(-1)
