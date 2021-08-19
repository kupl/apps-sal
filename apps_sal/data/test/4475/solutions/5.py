for _ in range(int(input())):
    (a, b, x, y, n) = list(map(int, input().split()))
    posa = max(a - n, x)
    posb = max(b - n, y)
    if posa < posb:
        n -= a - posa
        a = posa
        b = max(b - n, y)
    else:
        n -= b - posb
        b = posb
        a = max(a - n, x)
    print(a * b)
