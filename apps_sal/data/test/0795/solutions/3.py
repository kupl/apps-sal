def gcd(a, b):
    c = a % b
    return gcd(b, c) if c else b


n = int(input())
print(sum(n // (x * x + y * y) for x in range(1, int((n // 2) ** 0.5) + 1) for y in range(x + 1, int((n - x * x) ** 0.5) + 1, 2) if gcd(x, y) == 1))
