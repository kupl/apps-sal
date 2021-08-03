H, W = map(int, input().split())
c = [list(map(int, input().split())) for i in range(10)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            if c[i][j] > c[i][k] + c[k][j]:
                c[i][j] = c[i][k] + c[k][j]
s = 0
for i in range(H):
    a = list(map(int, input().split()))
    for j in range(W):
        if a[j] == -1:
            a[j] = 1
        s += c[a[j]][1]
print(s)
