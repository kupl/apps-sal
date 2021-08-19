ac = [[0 for i in range(2010)]for j in range(2010)]
n, k = map(int, input().split())
v = []
for i in range(n):
    v.append(input())
extra = 0
# row
for i in range(n):
    L = n
    R = -1
    for j in range(n):
        if v[i][j] == 'B':
            L = min(L, j)
            R = max(R, j)
    if L > R:
        extra += 1
    else:
        if R - L + 1 <= k:
            minx = max(0, i - k + 1)
            maxx = i
            miny = max(0, R - k + 1)
            maxy = L
            ac[minx][miny] += 1
            ac[maxx + 1][maxy + 1] += 1
            ac[maxx + 1][miny] -= 1
            ac[minx][maxy + 1] -= 1
for j in range(n):
    L = n
    R = -1
    for i in range(n):
        if v[i][j] == 'B':
            L = min(L, i)
            R = max(R, i)
    if L > R:
        extra += 1
    else:
        if R - L + 1 <= k:
            minx = max(0, R - k + 1)
            maxx = L
            miny = max(0, j - k + 1)
            maxy = j
            ac[minx][miny] += 1
            ac[maxx + 1][maxy + 1] += 1
            ac[maxx + 1][miny] -= 1
            ac[minx][maxy + 1] -= 1
for i in range(n):
    for j in range(n):
        if i > 0:
            ac[i][j] += ac[i - 1][j]
        if j > 0:
            ac[i][j] += ac[i][j - 1]
        if i > 0 and j > 0:
            ac[i][j] -= ac[i - 1][j - 1]
ans = 0
for i in range(n - k + 1):
    for j in range(n - k + 1):
        ans = max(ans, ac[i][j])
print(ans + extra)
