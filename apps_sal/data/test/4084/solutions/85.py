n, a, b = map(int, input().split())
c = a + b
print((n // c) * a + min(a, n % c))
