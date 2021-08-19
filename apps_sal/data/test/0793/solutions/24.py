def f(n, m):
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    dpi = [1] * (m + 1)
    for (i, sk) in enumerate(s):
        dpi1 = dpi[:]
        cs = 0
        for (j, tk) in enumerate(t):
            if sk == tk:
                cs = (cs + dpi[j]) % md
            dpi1[j + 1] = (dpi1[j + 1] + cs) % md
        dpi = dpi1
    print(dpi1[-1])


md = 10 ** 9 + 7
(n, m) = list(map(int, input().split()))
f(n, m)
