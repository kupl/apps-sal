n, a, b = list(map(int, input().split()))
if a * b >= 6 * n:
    print(a * b)
    print(a, b)
else:
    sq, ansx, ansy, ar = round(((6 * n)**0.5)), 1e9, 1e9, 1e18
    for i in range(1, sq + 6):
        p, q = i, (6 * n + i - 1) // i
        if max(p, q) >= max(a, b) and min(p, q) >= min(a, b):
            if ar > p * q:
                ar = p * q
                ansx, ansy = min(p, q), max(p, q)
    print(ansx * ansy)
    if ansx >= a and ansy >= b:
        print(ansx, ansy)
    else:
        print(ansy, ansx)
