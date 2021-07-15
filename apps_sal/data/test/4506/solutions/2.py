MOD = 998244353
n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
for i in range(n):
    a[i] = (a[i] * (n - i) * (i + 1))
a.sort(reverse = True)
b.sort()
res = 0
for i in range(n):
    a[i] %= MOD
    res += (a[i] * b[i]) % MOD
    res %= MOD
print(res)
