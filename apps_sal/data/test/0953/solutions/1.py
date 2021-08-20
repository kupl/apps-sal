n = int(input())
l = list(map(int, input().split()))
best = l
swaps = []
for i in range(n):
    p = list(input())
    for j in range(n):
        if j > i and p[j] == '1':
            swaps.append([i, j])
group = []
for i in range(n):
    group.append([i])
for i in range(len(swaps)):
    x = swaps[i][1]
    y = swaps[i][0]
    while isinstance(group[x], int) == 1:
        x = group[x]
    while isinstance(group[y], int) == 1:
        y = group[y]
    if y != x:
        group[y] += group[x]
        group[x] = y
for i in range(n):
    if isinstance(group[i], list) == 1:
        group[i] = sorted(group[i])
for i in range(n):
    if isinstance(group[i], list) == 1:
        x = []
        for j in range(len(group[i])):
            x.append(l[group[i][j]])
        x = list(sorted(x))
        for j in range(len(group[i])):
            l[group[i][j]] = x[j]
s = str(l[0])
for i in range(1, n):
    s += ' ' + str(l[i])
print(s)
