n, m = list(map(int, input().split()))
zn_kol = [0] * n
zn = [[] for i in range(n)]
zn_edge = [set() for i in range(n)]
ans = 100000000
for i in range(m):
    a, b = list(map(int, input().split()))
    zn_kol[a - 1] += 1
    zn_kol[b - 1] += 1
    zn_edge[a - 1].add(b - 1)
    zn_edge[b - 1].add(a - 1)
    zn[b - 1].append(a - 1)
    zn[a - 1].append(b - 1)
for i in range(n):
    for j in range(zn_kol[i] - 1):
        for z in range(j + 1, zn_kol[i]):
            if zn[i][j] in zn_edge[zn[i][z]]:
               if zn_kol[zn[i][j]] - 2 + zn_kol[zn[i][z]] - 2 + zn_kol[i] - 2 < ans:
                   ans = zn_kol[zn[i][j]] - 2 + zn_kol[zn[i][z]] - 2 + zn_kol[i] - 2
        
if ans == 100000000:
    print(-1)
else:
    print(ans)

