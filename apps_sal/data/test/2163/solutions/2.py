p = 10**9 + 7
n, m = map(int, input().split())

print(n + 1 if m == 1 else pow(m, n, p) * (1 + (pow(2 * m - 1, n, p) * pow(m, p - 1 - n, p) - 1) * m * pow(m - 1, p - 2, p)) % p)
