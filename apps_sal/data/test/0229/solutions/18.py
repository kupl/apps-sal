import sys
import math
n = int(input())
z = list(map(int, input().split()))
a = max(z)
b = min(z)
y = (a + b) // 2
x1 = a - y
x2 = a - b
flag = [0, 0, 0]
for i in range(n):
    if z[i] == y:
        flag[0] += 1
    else:
        if z[i] < y and z[i] + x1 == y:
            flag[0] += 1
        elif z[i] - x1 == y:
            flag[0] += 1
        if z[i] + x2 == a or z[i] == a:
            flag[1] += 1
        if z[i] - x2 == b or z[i] == b:
            flag[2] += 1
if flag.count(n) >= 1:
    print('YES')
else:
    print('NO')
