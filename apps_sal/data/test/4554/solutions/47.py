W, a, b = list(map(int, input().split()))

if (a <= b <= a + W) or (a <= b + W <= a + W):
    print((0))
    return

if a + W < b:
    print((b - (a + W)))
    return
else:
    print((a - (b + W)))

