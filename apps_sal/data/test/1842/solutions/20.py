(a, b, c) = [int(x) for x in input().split()]
z = (b ** 2 - 4 * a * c) ** 0.5
r1 = (-b - z) / (2 * a)
r2 = (-b + z) / (2 * a)
if r1 > r2:
    print(r1)
    print(r2)
else:
    print(r2)
    print(r1)
