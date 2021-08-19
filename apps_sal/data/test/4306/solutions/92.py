(a, b, c, d) = map(int, input().split())
if a <= c <= b <= d:
    print(b - c)
elif c <= a <= d <= b:
    print(d - a)
elif a <= c < d <= b:
    print(d - c)
elif c <= a < b <= d:
    print(b - a)
else:
    print(0)
