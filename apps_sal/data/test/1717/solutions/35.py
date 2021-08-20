n = int(input())


def gcd(u, v):
    if u < v:
        return gcd(v, u)
    if v == 0:
        return u
    return gcd(v, u % v)


x = 1
for i in range(1, n + 1):
    x = i // gcd(x, i) * x
print(x + 1)
