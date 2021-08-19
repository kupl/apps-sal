from sys import stdin
input = stdin.readline
MAX = 510000
MOD = 10 ** 9 + 7


def MakeTable():
    (fac[0], fac[1]) = (1, 1)
    (finv[0], finv[1]) = (1, 1)
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def COM(n, k):
    if n < k:
        return 0
    elif n < 0 or k < 0:
        return 0
    else:
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


(H, W, A, B) = map(int, input().split())
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX
N = min(H - A, W - B)
(x, y) = (0, 0)
result = 0
MakeTable()
for _ in range(N):
    n1 = H - A - 1 + B + x - y
    n2 = A + W - 1 - B - x + y
    result += COM(n1, B + x) * COM(n2, A + y) % MOD
    x += 1
    y += 1
print(result % MOD)
