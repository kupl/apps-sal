n = int(input())
p = list(range(n + 1))
c = [[i] for i in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    x, y = p[x], p[y]
    if len(c[x]) < len(c[y]):
        x, y = y, x
    c[x] += c[y]
    for z in c[y]:
        p[z] = x
print(*c[p[1]])
