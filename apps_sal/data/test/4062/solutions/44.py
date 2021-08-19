(a, b, c, d) = map(int, input().split())
if a < 0 and c < 0:
    print(max(a * c, b * d))
elif b < 0:
    print(b * c)
elif d < 0:
    print(a * d)
else:
    print(b * d)
