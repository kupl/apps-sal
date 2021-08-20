(n, a, b) = list(map(int, input().split()))
mod = 10 ** 9 + 7


def nCk(n, k):
    a = 1
    for i in range(n, n - k, -1):
        a *= i
        a %= mod
    b = 1
    for i in range(1, k + 1):
        b *= i
        b %= mod
    a *= pow(b, mod - 2, mod)
    return a


ans = pow(2, n, mod) - 1
ans -= nCk(n, a) + nCk(n, b)
print(ans % mod)
