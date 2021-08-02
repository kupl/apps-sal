n, k = map(int, input().split())


p = 10**9 + 7

fuct = [1]
for i in range(2000):
    fuct.append((fuct[i] * (i + 1)) % p)

for i in range(1, min(k, n - k + 1) + 1):
    Ca = (fuct[k - 1] * pow(fuct[i - 1], p - 2, p) * pow(fuct[k - i], p - 2, p)) % p
    Cb = (fuct[n - k + 1] * pow(fuct[i], p - 2, p) * pow(fuct[n - k + 1 - i], p - 2, p)) % p
    print((Ca * Cb) % p)
for i in range(min(k, n - k + 1) + 1, k + 1):
    print(0)
