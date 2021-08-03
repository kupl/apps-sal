
n = int(input())
cl = list(map(int, input().split()))
cl.sort(reverse=True)
MOD = 10**9 + 7

ans = 0
num = pow(2, n - 1, MOD)
inc = pow(2, n - 2, MOD)
for i in range(n):
    ans += num * cl[i]
    ans %= MOD
    num += inc
    num %= MOD

ans *= pow(2, n, MOD)
ans %= MOD
print(ans)
