from fractions import gcd
from sys import setrecursionlimit
setrecursionlimit(100000)
(n, d, h) = list(map(int, input().split()))
if n == 2:
    if d == 1 and h == 1:
        print('1 2')
    else:
        print('-1')
elif h < (d + 1) // 2 or d < 2:
    print('-1')
elif d == h == n - 1:
    for i in range(1, n):
        print(i, i + 1)
else:
    for i in range(1, h + 1):
        print(i, i + 1)
    if d == h:
        for i in range(h + 2, n + 1):
            print(2, i)
    else:
        print(1, h + 2)
        for i in range(h + 2, d + 1):
            print(i, i + 1)
        for i in range(d + 2, n + 1):
            print(1, i)
