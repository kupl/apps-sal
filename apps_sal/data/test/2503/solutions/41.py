(N, K) = (int(i) for i in input().split())
W = list()
for index in range(N):
    (x, y, c) = (s for s in input().split())
    x = int(x)
    y = int(y)
    c = 0 if c == 'W' else 1
    if x % (2 * K) != x % K:
        c = 1 - c
    if y % (2 * K) != y % K:
        c = 1 - c
    W.append((x % K, y % K, c))
w = [[0 for _ in range(K)] for _ in range(K)]
b = [[0 for _ in range(K)] for _ in range(K)]
wx = [0 for _ in range(K)]
wy = [0 for _ in range(K)]
bx = [0 for _ in range(K)]
by = [0 for _ in range(K)]
for (x, y, c) in W:
    if c == 0:
        w[x][y] += 1
        wx[x] += 1
        wy[y] += 1
    else:
        b[x][y] += 1
        bx[x] += 1
        by[y] += 1
M = 0
for row in w:
    M += sum(row)
s = M
for x in range(K):
    tmp = s
    for y in range(K):
        s += by[y]
        s -= wy[y]
        M = max(s, N - s, M)
    for y in range(K):
        by[y] += w[x][y]
        by[y] -= b[x][y]
        wy[y] += b[x][y]
        wy[y] -= w[x][y]
    tmp += bx[x]
    tmp -= wx[x]
    s = tmp
    M = max(s, N - s, M)
print(M)
