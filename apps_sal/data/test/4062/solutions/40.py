[a, b, c, d] = list(map(int, input().split()))

if (a > 0 and d < 0) or (b < 0 and c > 0):
    print((min(abs(a), abs(b)) * min(abs(c), abs(d))) * (-1))
else:
    print(max(a * c, a * d, b * c, b * d))
