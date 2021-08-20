(n, m) = [int(i) for i in input().split()]
kmin = 0
kmax = 0
kmin = (m - n % m) * (n // m) * (n // m - 1) // 2 + n % m * (n // m + 1) * (n // m) // 2
kmax = (n - m + 1) * (n - m) // 2
print(kmin, kmax)
