from math import *
for zz in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    ans = 0
    cs = 0
    for i in range(n):
        if a[i] < x:
            break
        ans += 1
        cs += a[i]
    if ans == n:
        print(n)
    elif ans == 0:
        print(0)
    else:
        h = ans
        ps = 0
        for i in range(ans, n):
            ps += a[i]
            if ps + cs < (i + 1) * x:
                break
            h += 1
        print(h)
