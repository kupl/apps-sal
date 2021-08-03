n = int(input())
l = [0] * n
d = [[]for _ in range(n)]
l[0] = 1
c = [0]
for _ in range(n - 1):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)
while c:
    x = c.pop()
    for y in d[x]:
        if not l[y]:
            c.append(y)
            l[y] = -1 * l[x]
r = l.count(1)
print(r * (n - r) - n + 1)
