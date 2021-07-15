from math import *
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z, x = list(map(int, input().split()))
    t, y = list(map(int, input().split()))
    lcd = x*y//gcd(x, y)
    if z < t:
        x, y, z, t = y, x, t, z
    w1 = z+t
    k = int(input())
    a.sort(reverse=True)
    l, r = -1, len(a)+1
    while r-l > 1:
        m = (l+r)//2
        w, ans = m//lcd, 0
        for q in range(w):
            ans += a[q]//100*w1
        for q in range(w, m//x):
            ans += a[q]//100*z
        for q in range(m//x, m//x+m//y-w):
            ans += a[q]//100*t
        if ans >= k:
            r = m
        else:
            l = m
    if r == len(a)+1:
        print(-1)
    else:
        print(r)

