def __starting_point():
    (a, b, x, y) = list(map(int, input().split()))
    ans = 0
    ud_sbn = abs(a - b)
    up = False
    if a - b < 0:
        up = True
    if ud_sbn == 0:
        ans = x
    elif up:
        u1 = ((ud_sbn + 1) * 2 - 1) * x
        u2 = x + ud_sbn * y
        ans = min(u1, u2)
    else:
        d1 = (ud_sbn * 2 - 1) * x
        d2 = x + (ud_sbn - 1) * y
        ans = min(d1, d2)
    print(ans)


__starting_point()
