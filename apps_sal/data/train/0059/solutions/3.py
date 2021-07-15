from math import *

zzz = int(input())
for zz in range(zzz):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = set()
    for i in range(n):
        if a[i] == -1:
            if i > 0:
                if a[i-1] >= 0:
                    b.add(a[i-1])
            if i < n - 1:
                if a[i+1] >= 0:
                    b.add(a[i+1])
    b = list(b)
    if len(b) == 0:
        print(0, 0)
    else:
        k = (min(b) + max(b)) // 2
        m = 0
        for i in range(n):
            if a[i] == -1:
                a[i] = k
        for i in range(1, n):
            m = max(m, abs(a[i-1]- a[i]))
        print(m, k)

