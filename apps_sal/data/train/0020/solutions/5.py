for t in range(int(input())):
    n, m = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    t0 = 0
    mi, ma = m, m
    f = True
    for t, l, h in a:
        delta = t - t0
        t0 = t
        mi -= delta
        ma += delta
        if mi <= l and ma >= h:
            mi = l
            ma = h
        elif l <= ma <= h and mi <= l:
            mi = l
            ma = ma
        elif l <= ma <= h and l <= mi <= h:
            mi = mi
            ma = ma
        elif ma >= h and l <= mi <= h:
            ma = h
            mi = mi
        else:
            f = False
    if f:
        print("YES")
    else:
        print("NO")

