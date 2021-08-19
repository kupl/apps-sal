(n, m) = list(map(int, input().split()))
mmax = (n - m) * (n - m + 1) // 2
mmin = 0
k = n // m
a = n % m
mmin = (k + 1) * k * a // 2 + (m - a) * k * (k - 1) // 2
print('{} {}'.format(mmin, mmax))
