a, b, c, d = list(map(int, input().split()))
if b <= d and a <= c:
    print((max(b - c, 0)))
elif b <= d and a > c:
    print((max(b - a, 0)))
elif b > d and a <= c:
    print((max(d - c, 0)))
else:
    print((max(d - a, 0)))
