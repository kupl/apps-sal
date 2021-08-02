n, m, h = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    target = b[i]
    for j in range(m):
        if c[i][j] == 0: continue
        if a[j] < target: continue
        c[i][j] = target
for j in range(m):
    target = a[j]
    for i in range(n):
        if c[i][j] == 0: continue
        if b[i] < target: continue
        c[i][j] = target
for row in c:
    for col in row:
        print(col, end=' ')
    print()
