from math import pi
import sys
sys.setrecursionlimit(10000000)
a = list(input())
b = list(input())
ab = a + list(reversed(b))
ab.remove('X')
a = list(input())
b = list(input())
cd = a + list(reversed(b))
cd.remove('X')
cd = cd + cd
friends = False
for i in range(3):
    good = True
    for j in range(3):
        if ab[j] != cd[i + j]:
            good = False
    friends = friends or good
if friends:
    print('YES')
else:
    print('NO')
