n = int(input())
ans = 0
MOD = int(10 ** 9 + 7)
a = [int(x) for x in input().split()]
a.sort()
po = [1]
for i in range(1, n):
    po.append(po[i - 1] * 2 % MOD)
for i in range(n):
    ans += a[i] * (po[i] - po[n - i - 1] + MOD)
    ans %= MOD
print(ans)
