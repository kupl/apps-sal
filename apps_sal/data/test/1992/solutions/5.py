n, m, k = list(map(int, input().split()))
p = [int(i) for i in input().split()]
u = [0 for i in range(n + 1)]
p += [0]
a = 0

for i in range(n, 0, -1):
    p[i] = p[i - 1]
for i in range(1, n + 1):
    u[p[i]] = i

for x in [int(i) for i in input().split()]:
    y = u[x]
    a += int((y - 1) / k) + 1
    if y < 2:
        continue
    p[y], p[y - 1] = p[y - 1], p[y]
    u[p[y]], u[p[y - 1]] = y, y - 1

print(a)
