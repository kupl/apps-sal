from math import *

mod = 1000000007

for zz in range(int(input())):
    n = int(input())
    a = [ int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ha = True
    hp = False
    hm = False
    for i in range(n):
        if b[i] != a[i]:
            if b[i] > a[i]:
                if (hp):
                    pass
                else:
                    ha = False
                    break
            else:
                if (hm):
                    pass
                else:
                    ha = False
                    break
        if a[i] > 0:
            hp = True
        elif a[i] < 0:
            hm = True

    if ha:
        print('YES')
    else:
        print('NO')

