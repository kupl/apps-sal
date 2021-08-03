n, m, a, b = list(map(int, input().split()))
print(min(a * (m - n % m), b * (n % m)))
