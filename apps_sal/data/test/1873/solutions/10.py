n, m = map(int, input().strip().split())
g = [0] * m
for a in map(int, input().strip().split()):
    g[a - 1] += 1

total = 0
for i in range(m):
    for j in range(i + 1, m):
        total += g[i] * g[j]

print(total)
