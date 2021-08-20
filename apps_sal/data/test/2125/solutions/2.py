(n, m) = list(map(int, input().split()))
A = [input() for _ in range(n)]
Dx = [[0] for _ in range(n)]
Dy = [[0] for _ in range(m)]
for i in range(n):
    last = None
    k = 0
    for j in range(m):
        c = A[i][j]
        if c != last:
            k = 0
        k += 1
        last = c
        Dx[i].append(k)
for j in range(m):
    last = None
    k = 0
    for i in range(n):
        c = A[i][j]
        if c != last:
            k = 0
        k += 1
        last = c
        Dy[j].append(k)
count = 0
for j in reversed(list(range(m))):
    col = Dy[j]
    i = len(col) - 1
    strips = []
    while i != 0:
        strips.append((col[i], i - col[i]))
        i -= col[i]
    for k in range(1, len(strips) - 1):
        if strips[k - 1][0] >= strips[k][0] <= strips[k + 1][0]:
            l = strips[k][1] - strips[k][0]
            r = strips[k - 1][1] + strips[k][0]
            res = min((Dx[i][j + 1] for i in range(l, r)))
            count += res
print(count)
