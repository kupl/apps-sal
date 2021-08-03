import fractions
n = int(input())
a = list(range(2, n + 1))


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


ans = a[0]

for i in range(n - 1):
    ans = ans * a[i] // fractions.gcd(ans, a[i])

print((ans + 1))
