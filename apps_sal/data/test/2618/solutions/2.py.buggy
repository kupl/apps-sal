from math import gcd


def check(m):
    nonlocal p, k, x, a, y, b
    ans = 0
    kx = m // a
    ky = m // b
    kxy = m // (a * b // gcd(a, b))
    kx -= kxy
    ky -= kxy
    for i in range(kxy):
        ans += p[i] * (x + y) // 100
        #print(p[i], end = ' ')
    if x >= y:
        for i in range(kxy, kxy + kx):
            ans += p[i] * x // 100
            #print(p[i],end = ' ')

        for i in range(kxy + kx, kxy + kx + ky):
            ans += p[i] * y // 100
            #print(p[i],end = ' ')
    else:
        for i in range(kxy, kxy + ky):
            ans += p[i] * y // 100
    #        print(p[i],end = ' ')

        for i in range(kxy + ky, kxy + kx + ky):
            ans += p[i] * x // 100
     #       print(p[i],end = ' ')
    # print("!!!!")
    #print('III', ans, m)
    return ans


p = []
for i in range(int(input())):
    n = int(input())
    p = sorted(map(int, input().split()), reverse=True)
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    k = int(input())
    l = 0
    r = n
    if check(n) < k:
        print(-1)
        # print()
        continue
    else:
        while r - l > 1:
            m = (r + l) // 2
            if check(m) >= k:
                r = m
            else:
                l = m
        print(r)
        # print()
