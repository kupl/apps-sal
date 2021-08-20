(n, m, a, b) = list(map(int, input().split()))
print(min(a * (n // m * m), b * (n // m)) + min(n % m * a, b))
