n = int(input())
ar = []
ar.append([1] * (n + 1))
for x in range(n - 1):
    ar.append([0] * (n + 1))
q = 0
for x in range(1, n):
    for y in range(1, n + 1):
        ar[x][y] = ar[x - 1][y] + ar[x][y - 1]
for x in range(n):
    q = max(q, max(ar[x]))
print(q)
