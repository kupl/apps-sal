MOD = 1000000007


def mod_pow(x, n):
    ret = 1
    while n > 0:
        if n & 1:
            ret = ret * x % MOD
        x = x * x % MOD
        n >>= 1
    return ret


(n, a, b) = [int(x) for x in input().split()]
ans = mod_pow(2, n) - 1
xa = n
for i in range(n - 1, n - a, -1):
    xa = xa * i % MOD
ya = a
for i in range(a - 1, 0, -1):
    ya = ya * i % MOD
xb = n
for i in range(n - 1, n - b, -1):
    xb = xb * i % MOD
yb = b
for i in range(b - 1, 0, -1):
    yb = yb * i % MOD
ca = xa * mod_pow(ya, MOD - 2) % MOD
cb = xb * mod_pow(yb, MOD - 2) % MOD
ans = (ans + MOD * 2 - ca - cb) % MOD
print(ans)
