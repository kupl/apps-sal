(n, m, a, b) = list(map(int, input().split()))

if n % m == 0:
    print(0)
else:
    k1 = n % m
    k2 = m - k1
    print(min(k1 * b, k2 * a))

