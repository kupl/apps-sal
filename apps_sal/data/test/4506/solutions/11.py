n = int(input())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
ans = 0
b.sort()
for i in range(n):
    k = (i + 1) * (n - i)
    a[i] *= k
a.sort()
for i in range(n):
    ans += b[n - i - 1] * a[i]
    ans %= 998244353
print(ans)
