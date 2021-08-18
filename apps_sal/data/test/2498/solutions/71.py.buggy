from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
l = [0] * n
for i in range(n):
    tmp = a[i]
    while tmp % 2 == 0:
        tmp //= 2
        l[i] += 1
    if i > 0 and l[i] != l[i - 1]:
        print((0))
        return
res = 1
for i in range(n):
    res = lcm(res, a[i] // 2)
print((m // res - m // (res * 2)))
