W, a, b = list(map(int, input().split()))

if a + W < b:
    print((b - (a + W)))
elif a > b + W:
    print((a - (b + W)))
else:
    print((0))
