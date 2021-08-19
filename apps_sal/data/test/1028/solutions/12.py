(n, m) = list(map(int, input().split()))


def pogatya(x):
    if x == 1:
        return 0
    else:
        return x * (x - 1) // 2


a = n // m
b = n % m
kmin = (m - b) * pogatya(a) + b * pogatya(a + 1)
kmax = pogatya(n - m + 1)
print(kmin, kmax)
