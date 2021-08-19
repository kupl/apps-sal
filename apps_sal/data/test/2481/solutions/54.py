(h, w) = map(int, input().split())
c = [list(map(int, input().split())) for i in range(10)]
for v in range(10):
    for s in range(10):
        for g in range(10):
            c[s][g] = min(c[s][g], c[s][v] + c[v][g])
a = [list(map(int, input().split())) for i in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == -1:
            continue
        ans += c[a[i][j]][1]
print(ans)
