def gcd(a, b):
    return gcd(b % a, a) if a else b


x, y, n = map(int, input().split())
d = gcd(x, y)
x, y = x // d, y // d
if n < y:
    d = [min(i, y - i) for i in ((x * i) % y for i in range(0, n + 1))]
    for i in range(n - 1, 0, -1):
        if d[i] < d[n] and n * d[i] <= i * d[n]:
            n = i
    print(str((x * n) // y + int(2 * ((x * n) % y) > y)) + '/' + str(n))
else:
    print(str(x) + '/' + str(y))
