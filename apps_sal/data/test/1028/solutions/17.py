def ap(n):
    return n * (n - 1) // 2


(n, m) = map(int, input().split())
kmax = ap(n - m + 1)
if m == 1:
    kmin = kmax
else:
    kmin = ap(n // m + 1) * (n % m) + ap(n // m) * (m - n % m)
print(kmin, kmax)
