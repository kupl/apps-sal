(n, s) = map(int, input().split())
d = {}
for i in range(n - 1):
    vertex = list(map(int, input().split()))
    d[vertex[0]] = d.get(vertex[0], 0) + 1
    d[vertex[1]] = d.get(vertex[1], 0) + 1
c = 0
for i in d:
    if d[i] == 1:
        c += 1
print(2 * s / c)
