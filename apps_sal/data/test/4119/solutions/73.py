n, m, *a = list(map(int, open(0).read().split()))
a.sort()
b = []
for i in range(m - 1):
    b.append(a[i + 1] - a[i])
b.sort()
ans = 0
for i in range(m - n):
    ans += b[i]
print(ans)

