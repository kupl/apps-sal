for t in range(int(input())):
    (n, x, m) = list(map(int, input().split()))
    inf = x
    sup = x
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        if a <= inf <= b:
            sup = max(sup, b)
            inf = min(inf, a)
        if a <= sup <= b:
            inf = min(inf, a)
            sup = max(sup, b)
    print(sup - inf + 1)
