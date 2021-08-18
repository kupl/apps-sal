import math

s = input()
ans = 0
u = 0
d = 0
l = 0
r = 0
if len(s) % 2 != 0:
    print('-1')
else:
    for i in s:
        if i == 'D':
            d += 1
        elif i == 'U':
            u += 1
        elif i == 'L':
            l += 1
        elif i == 'R':
            r += 1
    print(int((abs(r - l) + abs(u - d)) / 2))
