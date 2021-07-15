import sys


MOD = 1_000_000_007


X, Y = [int(x) for x in input().split()]


def mod_pow(x, n):
    ret = 1
    while n > 0:
        if n & 1:
            ret = ret * x % MOD
        x = x * x % MOD
        n >>= 1
    return ret


z = X + Y
if z % 3 != 0:
    print((0))
    return

n = z // 3
k = -1
for i in range(n, z - n + 1):
    if X == i or Y == i:
        k = z - n - i
        break
if k == -1:
    print((0))
    return
a = n
for i in range(n - 1, n - k, -1):
    a = a * i % MOD
b = k
for i in range(k - 1, 0, -1):
    b = b * i % MOD
ans = a * mod_pow(b, MOD - 2) % MOD
print(ans)

