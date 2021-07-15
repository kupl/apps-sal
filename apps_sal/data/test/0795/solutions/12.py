def gcd(a, b):

    c = a % b

    return gcd(b, c) if c else b



n = int(input())

a, b = int((n // 2) ** 0.5) + 1, int((n - 1) ** 0.5) + 1

print(sum(n // (x * x + y * y) for x in range(1, a) for y in range(x + 1, b, 2) if gcd(x, y) == 1))
