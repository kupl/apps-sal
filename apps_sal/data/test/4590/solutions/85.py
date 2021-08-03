n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, i, j = 0, 0, 0
a.append(10**9 + 1)
b.append(10**9 + 1)
while x + a[i] <= k:
    x += a[i]
    i += 1
maxs = i
for c in range(n + m):
    if x + b[j] <= k:
        x += b[j]
        j += 1
        maxs = max(maxs, i + j)
    else:
        if i > 0:
            x = max(0, x - a[i - 1])
            i -= 1
print(maxs)
