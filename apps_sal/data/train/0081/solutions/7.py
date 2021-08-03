from math import *

zzz = int(input())
for zz in range(zzz):
    a = input()
    b = input()
    c = input()
    ha = True
    for i in range(len(a)):
        if not b[i] == c[i] and not a[i] == c[i]:
            ha = False
            break
    if not ha:
        print('NO')
    else:
        print('YES')
