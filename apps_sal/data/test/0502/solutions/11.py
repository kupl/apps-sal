a, b, c, d, e, f = map(int, input().split())
k = (c - e) ** 2 + (d - f) ** 2
if (a - c) ** 2 + (b - d) ** 2 == k and (a - e) ** 2 + (b - f) ** 2 != k * 4:
    print("Yes")
else:
    print("No")
