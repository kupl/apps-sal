def R():
    return map(int, input().split())


(a, b, n) = R()
for _ in range(n):
    (l, t, m) = R()
    (ll, rr) = (l - 1, 10 ** 6 + 7)
    sl = a + (l - 1) * b
    while ll < rr:
        mm = (ll + rr + 1) // 2
        sr = a + (mm - 1) * b
        slr = (sl + sr) * (mm - l + 1) // 2
        if slr <= t * m and sr <= t:
            ll = mm
        else:
            rr = mm - 1
    if ll >= l:
        print(ll)
    else:
        print(-1)
