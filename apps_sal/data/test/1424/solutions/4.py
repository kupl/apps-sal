n, m, k = map(int, input().split())
a = []
ans = 0
for i in range(m):
    a.append(int(input()))
s = int(input())
r = []
for i in range(n):
    r.append(s % 2)
    s = s // 2
for i in range(m):
    j = 0
    c = 0
    g = a[i]
    while j < n and c <= k:
        if r[j] == g % 2:
            j += 1
        else:
            j += 1
            c += 1
        g = g // 2
    if c <= k:
        ans += 1
print(ans)
