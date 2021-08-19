(n, m) = map(int, input().split())
(i, j) = (2, n)
for k in range(m):
    (x, y) = map(int, input().split())
    if x > y:
        (x, y) = (y, x)
    (i, j) = (max(i, x + 1), min(j, y))
print(max(j - i + 1, 0))
