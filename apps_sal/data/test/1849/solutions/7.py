MOD = 998244353
n = int(input())
ans = []
for i in range(1, n):
    res = 0
    res += 180 * pow(10, n - 1 - i, MOD)
    if i + 2 <= n:
        res += 810 * (n - 1 - i) * pow(10, n - 2 - i, MOD)
    ans.append(res % MOD)
ans.append(10)
print(*ans)
