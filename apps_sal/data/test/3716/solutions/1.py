n = int(input())
res = n * (n - 1)
def gcd(a, b): return b if a % b == 0 else gcd(b, a % b)


for i in range(n - 2 if n % 2 != 0 else n - 3, 0, -2):
    if gcd(n, i) == 1 and gcd(n - 1, i) == 1:
        res = res * i if n % 2 != 0 else max(res * i, int(res / 2) * (n - 2),
                                             (n - 1) * (n - 2) * (n - 3))
        break

if n < 3:
    res = n

print(res)
