(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
m -= 1
ans = 1000
for i in range(m, -1, -1):
    if a[i] and a[i] <= k:
        ans = m - i
        break
for i in range(m, n):
    if a[i] and a[i] <= k:
        ans = min(ans, i - m)
        break
print(ans * 10)
