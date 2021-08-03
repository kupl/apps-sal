b, d, s = list(map(int, input().split()))

if b > d and b > s:
    print((b - 1) - d + (b - 1) - s)
elif d > b and d > s:
    print((d - 1) - b + (d - 1) - s)
elif s > b and s > d:
    print((s - 1) - b + (s - 1) - d)
elif b == d and b > s:
    print(max(0, (b - 1) - s))
elif d == s and d > b:
    print(max(0, (d - 1) - b))
elif b == s and b > d:
    print(max(0, (b - 1) - d))
else:
    print(0)
