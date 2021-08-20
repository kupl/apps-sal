mod = 1000000007
fact = [1] * 2000
for i in range(1, 2000):
    fact[i] = fact[i - 1] * i % mod
(n, m) = list(map(int, input().split()))
a = sorted(map(int, input().split()))
b = []
for i in range(1, m):
    x = a[i] - a[i - 1] - 1
    if x > 0:
        b.append(x)
count = pow(2, sum(b) - len(b), mod) * fact[n - m] % mod
b = [a[0] - 1] + b + [n - a[-1]]
for i in b:
    count = count * pow(fact[i], mod - 2, mod) % mod
print(count)
