MOD = 1000000009


def Pow(base, n):
    res = 1
    while n:
        if n & 1:
            res = (res * base) % MOD
        base = (base * base) % MOD
        n >>= 1
    return res


n, a, b, k = list(map(int, input().split()))
ans = 0
num = (n + 1) // k
_a = Pow(a, MOD - 2)
q = Pow(b, k) * Pow(Pow(a, k), MOD - 2) % MOD
if q == 1:
    res = Pow(a, n) * num % MOD
    for i in input():
        if i == '+':
            ans = (ans + res) % MOD
        else:
            ans = (ans - res) % MOD
        res = res * b % MOD * _a % MOD
else:
    rat = (Pow(q, num) - 1) % MOD * Pow((q - 1) % MOD, MOD - 2) % MOD
    cur = Pow(a, n) * rat % MOD
    for i in input():
        if i == '+':
            ans = (ans + cur) % MOD
        else:
            ans = (ans - cur) % MOD
        cur = cur * b % MOD * _a % MOD
print(ans)
