W, a, b = list(map(int, input().split()))
if b >= a:
    if b - (a + W) < 0:
        print((0))
    else:
        print((b - (a + W)))
else:
    if a - (b + W) < 0:
        print((0))
    else:
        print((a - (b + W)))
