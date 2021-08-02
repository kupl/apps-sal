n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] * (i + 1) * (n - i)
a = sorted(a)
b = sorted(b)
ans = 0
for i in range(n):
    ans += b[n - i - 1] * a[i] % 998244353
    ans %= 998244353
print(ans)
