(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * (n + 1)
d = [0] * (m + 1)
for i in range(n):
    c[i + 1] = a[i] + c[i]
for i in range(m):
    d[i + 1] = b[i] + d[i]
for i in range(m + 1)[::-1]:
    if d[i] <= k:
        x = i
        break
ans = x
for i in range(1, n + 1):
    while c[i] + d[x] > k:
        if x >= 1:
            x -= 1
        else:
            break
    if c[i] + d[x] <= k:
        ans = max(ans, i + x)
print(ans)
