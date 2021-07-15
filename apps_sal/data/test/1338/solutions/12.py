import sys
n, k = [int(i) for i in input().split()]
m = 0
a = [True for i in range(n+1)]
l = [0 for i in range(n+1)]
big = 0
for x in range(1,n+1):
    for y in range(x,n+1):
        big += x
def r(i):
    if i > n:
        f = 0
        for x in range(1,n+1):
            u = l[x]
            for y in range(x,n+1):
                u = min(u, l[y])
                f += u
        nonlocal m
        if f == big:
            m += 1
        if m == k:
            for j in range(1,n+1):
                print(l[j], end = ' ')
            return
        return 0
    for j in range(1,n+1):
        if a[j]:
            a[j] = False
            l[i] = j
            r(i+1)
            a[j] = True
    return 0

r(1)
