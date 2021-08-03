n, m = list(map(int, input().split()))


def pa(a):
    return a * (a - 1) // 2


ma = pa(n - m + 1)

t = n % m
mi = pa(n // m) * (m - t) + pa(n // m + 1) * t

print(mi, ma)
