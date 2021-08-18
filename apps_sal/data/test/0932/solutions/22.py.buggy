m, n = (int(x) for x in input().split())
b = []
r1 = []
for i in range(m):
    b.append([int(x) for x in input().split()])
    r1.append(sum(b[i]) == n)
c1 = [sum(b[i][j] for i in range(m)) == m for j in range(n)]
if (sum(r1) == 0 and sum(c1)) != 0 or (sum(r1) != 0 and sum(c1) == 0):
    print('NO')
    return
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        if b[i][j] == 0:
            a[i].append(0)
        elif not r1[i] and not c1[j]:
            print('NO')
            return
        else:
            a[i].append(1 if r1[i] and c1[j] else 0)
print('YES')
for i in range(m):
    print(' '.join(map(str, a[i])))
