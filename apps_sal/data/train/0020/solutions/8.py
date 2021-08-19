Q = int(input())
for _ in range(Q):
    (n, m) = map(int, input().split())
    (lt, mn, mx) = (0, m, m)
    ok = True
    for i in range(n):
        if ok:
            (t, l, h) = map(int, input().split())
            mn = max(mn - (t - lt), l)
            mx = min(mx + (t - lt), h)
            lt = t
            if mn > mx:
                ok = False
        else:
            input()
    print('YES' if ok else 'NO')
