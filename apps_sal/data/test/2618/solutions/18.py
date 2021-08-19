from math import gcd

q = int(input())
for i in range(q):
    n = int(input())
    p = sorted(map(int, input().split()), key=int)[::-1]
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    k = int(input())

    # preprocessing
    c = a * b // gcd(a, b)
    if y > x:
        x, y = y, x
        a, b = b, a

    # aux fxn to find whether m tickets suffice
    def check(m):
        add = 0
        hc = m // c
        ha = m // a - hc
        hb = m // b - hc
        # print("aajo")
        # print(m,hc,ha,hb)
        for j in range(hc):
            add += (x + y) * p[j] // 100
        for j in range(hc, hc + ha):
            add += x * p[j] // 100
        for j in range(hc + ha, hc + ha + hb):
            add += y * p[j] // 100

        return add

    # lower bound using check fxn
    lo, hi = 1, n
    ans = -1

    while(lo <= hi):
        mid = (lo + hi) // 2
        val = check(mid)
        # print("check")
        #print(mid, val)
        if val >= k:
            ans = mid
            hi = mid - 1
        # elif val > k:
        #    ans = mid
        #    hi = mid - 1
        else:
            lo = mid + 1

    print(ans)
