n = int(input())
p = {}
for x in range(1, int((n // 2) ** 0.5) + 1):
    for y in range(x + 1, int((n - x * x) ** 0.5) + 1):
        for k in range(1, n // (x * x + y * y) + 1):
            (a, b) = (k * (y * y - x * x), 2 * y * x * k)
            if a > b:
                (a, b) = (b, a)
            p[a, b] = 0
print(len(p))
