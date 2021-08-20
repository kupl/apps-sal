(n, m) = map(int, input().split())
c = [[] for _ in range(n)]
for i in range(m):
    (p, y) = map(int, input().split())
    c[p - 1].append([i, y])
ans = [0] * m
for i in range(n):
    c[i].sort(key=lambda x: x[1])
    for j in range(len(c[i])):
        ID = str(i + 1).zfill(6) + str(j + 1).zfill(6)
        ans[c[i][j][0]] = ID
print(*ans, sep='\n')
