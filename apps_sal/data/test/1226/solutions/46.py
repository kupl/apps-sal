def ncr(n, r, p):
    num = 1
    den = 1
    for i in range(r):
        num = num * (n - i) % p
        den = den * (i + 1) % p
    return num * pow(den, p - 2, p) % p


(n, a, b) = list(map(int, input().split()))
m = 1000000007
print((pow(2, n, m) - 1 - ncr(n, a, m) - ncr(n, b, m)) % m)
