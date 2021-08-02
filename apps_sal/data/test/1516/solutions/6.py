MOD = 998244353
n = int(input())
a = [int(w) for w in input().split()]


def pad(x, k):
    e = 1
    r = 0
    while x > 0:
        r += e * (x % 10)
        x //= 10
        e *= 100 if k > 0 else 10
        k -= 1
    return r


r = 0
for x in a:
    r = (r + pad(x, 57)) % MOD

print(r * n * 11 % MOD)
