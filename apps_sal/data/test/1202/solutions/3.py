n = int(input())
(a, b) = ([0] * n, [0] * n)
for i in range(n):
    (a[i], b[i]) = map(int, input().split())
k = n // 2
i = j = k - 1
if 2 * k < n:
    if a[k] < b[k]:
        (i, j) = (k, k - 1)
    else:
        (i, j) = (k - 1, k)
(x, y) = (i + 1, j)
while x < n and y >= 0 and (a[x] < b[y]):
    x += 1
    y -= 1
(u, v) = (i, j + 1)
while u >= 0 and v < n and (a[u] > b[v]):
    u -= 1
    v += 1
(i, j) = (max(i, x), max(j, v))
print('1' * i + '0' * (n - i))
print('1' * j + '0' * (n - j))
