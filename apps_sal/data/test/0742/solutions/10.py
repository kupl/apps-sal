from math import *

zzz = int(input())
for zz in range(zzz):
    n = int(input())
    b = [int(i) for i in input().split()]
    a = [0] * (2 * n)
    sl = set([i + 1 for i in range(2 * n)])
    ha = True
    for i in range(n):
        a[2 * i] = b[i]
        try:
            sl.remove(b[i])
        except:
            ha = False
            break
    if ha:
        sl = list(sl)
        sl.sort()
        for i in range(n):
            j = 0
            while j < len(sl) and sl[j] < b[i]:
                j += 1
            if j == len(sl):
                ha = False
                break
            else:
                a[2 * i + 1] = sl.pop(j)

    if ha:
        print(' '.join(map(str, a)))
    else:
        print(-1)
