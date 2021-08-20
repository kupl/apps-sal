import math


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


n = int(input())
res = 0
m = int(math.sqrt(n))
for i in range(1, m + 1):
    for j in range(i, m + 1):
        k = i * i + j * j
        if k > n:
            break
        if (j - i) % 2 == 0 or gcd(i, j) != 1:
            continue
        res += n // k
print(res)
