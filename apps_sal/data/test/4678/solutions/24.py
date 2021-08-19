n = int(input())
a = list(map(int, input().split()))
m = 0
ans = 0
for i in range(n - 1):
    if a[i] > m:
        m = a[i]
    if a[i + 1] < m:
        ans += m - a[i + 1]
        a[i + 1] = m
print(ans)
