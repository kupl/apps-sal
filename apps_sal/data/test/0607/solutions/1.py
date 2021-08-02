input = __import__('sys').stdin.readline
MIS = lambda: map(int, input().split())

n, MOD = MIS()
ans = 0
fac = [1]
for i in range(1, n + 2): fac.append(fac[-1] * i % MOD)
for d in range(1, n + 1):
    ans += (n - d + 1)**2 * fac[d] * fac[n - d]
    ans %= MOD
print(ans)
