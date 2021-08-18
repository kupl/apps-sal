from fractions import gcd

n, x, d = list(map(int, list(input().split())))

if d == 0:
    if x == 0:
        print((1))
    else:
        print((n + 1))

else:

    if d < 0:
        d, x = -d, -x

    g = gcd(d, abs(x))
    d, x = d // g, x // g

    klist = list(range(n + 1))
    klist.sort(key=lambda k: (k * x % d, k))

    ans = 0

    pmin, pmax = 1, 0
    pmd = -1
    for k in klist:
        tmin = (k * x + (k - 1) * k // 2 * d) // d
        tmax = (k * x + (2 * n - k - 1) * k // 2 * d) // d
        tmd = k * x % d

        if tmd == pmd and tmin <= pmax and tmax >= pmin:
            pmin, pmax = min(pmin, tmin), max(pmax, tmax)
        else:
            ans += pmax - pmin + 1
            pmin, pmax = tmin, tmax
        pmd = tmd

    ans += pmax - pmin + 1
    print(ans)
