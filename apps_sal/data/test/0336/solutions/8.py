n, a, b, c, d = map(int, input().split())
q = {}
for x1 in range(1, n + 1):
    x4 = a + x1 - d
    if x4 < 1 or x4 > n:
        continue
    x2 = x1 + b - c
    if x2 < 1 or x2 > n:
        continue
    x5 = x2 + a - d
    if x5 < 1 or x5 > n:
        continue
    q[(x1, x2, x4, x5)] = 1
print(len(q) * n)
