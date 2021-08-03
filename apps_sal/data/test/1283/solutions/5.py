def make():
    s = ''
    for x in range(j, j + k):
        s += field[x][i]
    return s


n, k = map(int, input().split())
field = []
for i in range(n):
    field.append(input())
best = []
for i in range(n):
    best.append([0] * n)
for i in range(n):
    for j in range(n - k + 1):
        if field[i][j: j + k] == '.' * k:
            for x in range(j, j + k):
                best[i][x] += 1
for i in range(n):
    for j in range(n - k + 1):
        s = make()
        if s == '.' * k:
            for x in range(j, j + k):
                best[x][i] += 1
ind1 = 0
ind2 = 0
ans = -19942347392
for i in range(n):
    for j in range(n):
        if best[i][j] > ans:
            ans = best[i][j]
            ind1 = i
            ind2 = j
if ans > 0:
    print(ind1 + 1, ind2 + 1)
else:
    print(1, 1)
