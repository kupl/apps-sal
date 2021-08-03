from math import gcd

for _ in range(int(input())):
    m, d, w = list(map(int, input().split()))
    if d == 1:
        print(0)
    else:
        w1 = w // gcd(w, d - 1)
        md = min(m, d)
        # sum(max(md - w1 * n, 0) for n in 1..inf)
        # sum(md - w1 * n for n in 1..md // w1)
        mdd_w1 = md // w1
        print((md * 2 - w1 - mdd_w1 * w1) * mdd_w1 // 2)
