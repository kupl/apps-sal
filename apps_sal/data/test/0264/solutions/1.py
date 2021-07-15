mod = 1000000007
def power(a, p):
    res = 1
    while p > 0:
        if p % 2 == 1:
            res = (res * a) % mod
        a = (a * a) % mod
        p //= 2
    return res
n, m = map(int, input().split())
n += 1
res = (power(n * 2, m - 1)) * (n - m) * 2
print(res % mod)
