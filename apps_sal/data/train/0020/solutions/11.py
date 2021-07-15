q = int(input())
for _ in range(q):
    n,m = list(map(int, input().split()))
    customers = [[int(x) for x in input().split()] for _ in range(n)]

    now_l, now_h = m, m
    now = 0
    for t,l,h in customers:
        dt = t - now

        # in area?
        next_h = min(now_h + dt, h)
        next_l = max(now_l - dt, l)
        if not next_l <= next_h:
            ok = False
            break

        now = t
        now_l, now_h = next_l, next_h
    else:
        ok = True

    print("YES" if ok else "NO")

