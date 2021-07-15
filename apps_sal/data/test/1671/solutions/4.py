n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
for i in range(n):
    sum += a[i]
z1 = sum // n
z2 = sum // n + 1
col = sum % n
col = n - col
ans = 0
for i in range(col):
    ans += abs(z1 - a[i])
for t in range(col, n):
    ans += abs(a[t] - z2)
print(ans // 2)

