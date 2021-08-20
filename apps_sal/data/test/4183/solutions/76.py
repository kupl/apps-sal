n = int(input())
a = []
for i in range(n):
    a.append(int(input()))


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


res = a[0]
for i in range(n):
    res = res * a[i] // gcd(res, a[i])
print(res)
