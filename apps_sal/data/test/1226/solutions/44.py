n, a, b = list(map(int, input().split()))


def pow(x, n, m):
    if n == 0:
        return 1
    res = pow(x * x % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


c = max(a, b)
inv = [0 for i in range(c + 1)]
finv = [0 for i in range(c + 1)]
inv[1] = 1
finv[0] = finv[1] = 1
for i in range(2, c + 1):
    inv[i] = 1000000007 - (1000000007 // i) * inv[1000000007 % i] % 1000000007
    finv[i] = finv[i - 1] * inv[i] % 1000000007


def kaizyou(k):
    num = 1
    for i in range(n - k + 1, n + 1):
        num = num * i % 1000000007
    return num


def combinations(k):
    return kaizyou(k) * finv[k] % 1000000007


print(((pow(2, n, 1000000007) - combinations(a) - combinations(b) - 1) % 1000000007))
