n = int(input())
c = list(map(int, input().split()))
c.sort()
MOD = 1000000007
ans = 0
P = pow(4, n - 1, MOD)
if n == 1:
    ans = c[0] * 2 % MOD
else:
    for i in range(n):
        ans += P * c[i] * (n + 1 - i)
        ans %= MOD
print(ans)
