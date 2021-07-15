h, w = map(int, input().split())
a = []
c = []
for i in range(10):
    c.append(list(map(int, input().split())))
for i in range(h):
    a.append(list(map(int, input().split())))


for k in range(10):
    for i in range(10):
        for j in range(10):
            if c[i][j] > c[i][k] + c[k][j]:
                c[i][j] = c[i][k] + c[k][j]
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] >= 0:
            ans += c[a[i][j]][1]

print(ans)
