a, b, n, x = list(map(int, input().split()))
m = 10**9 + 7
print(((pow(a, n, m) * x + b * (pow(a, n, m) - 1) * pow(a - 1, m - 2, m)) if a != 1 else b * n + x) % m)
