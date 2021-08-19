n = int(input())
s = input()
g = {}
src = 0
for i in s.split():
    g[src] = [int(i) - 1]
    if src > 0:
        g[src].append(src - 1)
    if src < n - 1:
        g[src].append(src + 1)
    src += 1
energy = [-1] * n
q = []
q.append(0)
energy[0] = 0
while len(q) > 0:
    x = q.pop(0)
    for y in g[x]:
        if energy[y] == -1:
            energy[y] = energy[x] + 1
            q.append(y)
for i in energy:
    print(i, end=' ')
