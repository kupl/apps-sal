from collections import defaultdict
g = defaultdict(list)
row = defaultdict(int)
column = defaultdict(int)
ng = defaultdict(list)
gg = defaultdict(list)


n, m = (int(x) for x in input('').split())
for i in range(n):
    g[i] = [int(x) for x in input('').split()]
    ng[i] = [0] * m
    gg[i] = [0] * m
for i in range(n):
    row[i] = all(g[i])
for j in range(m):
    column[j] = all(g[i][j] for i in range(n))

for i in range(n):
    for j in range(m):
        ng[i][j] = int(row[i] and column[j])

for i in range(n):
    if any(ng[i]):
        gg[i] = [1] * m

for j in range(m):
    if any(ng[i][j] for i in range(n)):
        for i in range(n):
            gg[i][j] = 1


# print(g)
# print(row)
# print(column)
# print(ng)
# print(gg)
if gg == g:
    print('YES')
    for i in range(n):
        print(' '.join(str(x) for x in ng[i]))
else:
    print('NO')
