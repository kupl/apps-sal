(n, m, a, b) = (int(x) for x in input().split())
print(min(a * n, (n + m - 1) // m * b, n // m * b + n % m * a))
