MAX = 1000010
finv = [0] * MAX
inv = [0] * MAX


def COMinit():
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def COM(n, k):
    res = 1
    for i in range(k):
        res = res * (n - i) % MOD
    return res * finv[k] % MOD


MOD = 10 ** 9 + 7
(x, y) = map(int, input().split())
(s, t) = ((-x + 2 * y) / 3, (2 * x - y) / 3)
if s < 0 or t < 0:
    ans = 0
elif not (s.is_integer() and t.is_integer()):
    ans = 0
else:
    (s, t) = (int(s), int(t))
    COMinit()
    ans = COM(s + t, s)
print(ans)
