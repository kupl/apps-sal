(n, s) = map(int, input().split())
a = [0] * (n + 1)
kol = 0
for i in range(n - 1):
    (x, y) = map(int, input().split())
    a[x] += 1
    a[y] += 1
for i in range(1, n + 1):
    if a[i] == 1:
        kol += 1
print(s / kol * 2)
