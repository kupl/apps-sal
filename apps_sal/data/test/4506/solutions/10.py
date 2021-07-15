n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(n):
    c.append(a[i] * (n - i) * (i + 1))
c.sort()
b.sort(reverse=True)
ans = 0
for i in range(n):
    ans = (ans + c[i] * b[i]) % 998244353
print(ans)
