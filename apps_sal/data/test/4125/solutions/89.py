n, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(n):
    a[i] = abs(a[i] - x)


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


res = a[0]
for i in range(n):
    res = gcd(res, a[i])
print(res)
