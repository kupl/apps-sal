n, m, k = map(int, input().split())
t = [[0] * m for i in range(n)]
used = set()
a = []
for i in range(k):
    q, b, c = tuple(map(int, input().split()))
    b = b - 1
    a.append((q, b, c))

a = a[::-1]
for i in range(k):
    if a[i][0:2] not in used:
        if a[i][0] == 1:
            for s in range(m):
                if t[a[i][1]][s] == 0:
                    t[a[i][1]][s] = a[i][2]
        else:
            for s in range(n):
                if t[s][a[i][1]] == 0:
                    t[s][a[i][1]] = a[i][2]
        used.add(a[i][0:2])
for i in range(n):
    for j in range(m):
        print(t[i][j], end=' ')
    print()
