N, M = list(map(int, input().split()))
a = []; b = []; c = []; d = []

for i in range(N):
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)
for i in range(M):
    x, y = list(map(int, input().split()))
    c.append(x)
    d.append(y)

for i in range(N):
    m = abs(a[i] - c[0]) + abs(b[i] - d[0])
    p = 0
    for j in range(1, M):
        if m > abs(a[i] - c[j]) + abs(b[i] - d[j]):
            m = abs(a[i] - c[j]) + abs(b[i] - d[j])
            p = j
    print((p + 1))

