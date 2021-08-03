# C
n = int(input())
mod = 10e8 + 7


def powmod(x, y):
    res = 1
    for _ in range(y):
        res *= x
        res %= mod
    return res


ans = powmod(10, n) - powmod(9, n) - powmod(9, n) + powmod(8, n)

ans %= mod
ans = int(ans)
print(ans)
