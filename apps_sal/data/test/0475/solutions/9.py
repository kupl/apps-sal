(n, m, k) = list(map(int, input().split()))
ans = 1
for i in range(1, k + 1):
    ans *= n - i
for i in range(k, 0, -1):
    ans //= i
ans = ans * m % 998244353
for i in range(k):
    ans = ans * (m - 1) % 998244353
print(ans)
