from math import *
for zz in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    i = 0
    j = n - 1
    ans = 0
    ct = 0
    ps = 0
    x = 0
    y = 0
    while i <= j:
        cs = 0
        if ct == 0:
            while i <= j and cs <= ps:
                cs += a[i]
                i += 1
            x += cs
        else:
            while i <= j and cs <= ps:
                cs += a[j]
                j -= 1
            y += cs
        ps = cs
        ct = 1 - ct
        ans += 1
    print(ans, x, y)
