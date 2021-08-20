def intSqrt(x):
    a = 1
    b = x
    while a < b:
        c = (a + b) // 2
        if c * c > x:
            b = c
        elif abs(c * c - x) < 0.1:
            a = c
            break
        else:
            a = c + 1
    return a


a = [int(x) for x in input().split()]
area = sum([a[i] * a[i + 1] for i in range(0, 6, 2)])
sides = [(a[i] ** 2 + a[i + 1] ** 2 + a[i] * a[i + 1]) ** 0.5 for i in range(0, 6, 2)]
semi = sum(sides) / 2
print(area + int(intSqrt(16 * semi * (semi - sides[0]) * (semi - sides[1]) * (semi - sides[2]) / 3)))
