from math import *

for zz in range(int(input())):
    n = int(input())
    if n % 4 != 0:
        print('NO')
    else:
        print('YES')
        a = []
        cs = 0
        ce = 2
        for i in range(n//2):
            a.append(ce)
            cs += ce
            ce += 2
        ce = 1
        for i in range(n//2, n - 1):
            a.append(ce)
            cs -= ce
            ce += 2
        a.append(cs)
        print(*a)

