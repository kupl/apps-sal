n, m = map(int, input().split())
kmin = (n // m + 1) * (n // m) // 2 * (n % m) + (n // m) * (n // m - 1) // 2 * (m - n % m)
kmax = (n - m + 1) * (n - m) // 2
print(kmin, kmax)
