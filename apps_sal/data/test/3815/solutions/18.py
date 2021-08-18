n, a, b, k = list(map(int, input().split()))
s = str(input())
MOD = 10**9 + 9


def fun(a, b, i):
    return (pow(a, n - i, MOD) * pow(b, i, MOD)) % MOD


def div(x, y):
    return (x * pow(y, MOD - 2, MOD)) % MOD


r = pow(div(b, a), k, MOD)
SUM = 0

for i in range(k):
    if s[i] == '-':
        SUM += -1 * fun(a, b, i)
    else:
        SUM += +1 * fun(a, b, i)

n += 1
t = n // k

ans = pow(r, t, MOD) - 1
x = r - 1
if x:
    ans = (div(ans, x) * SUM) % MOD
else:
    ans = (t * SUM) % MOD
ans += MOD
ans %= MOD
print(ans)
