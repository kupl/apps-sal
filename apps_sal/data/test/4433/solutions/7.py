n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(m)]

b = [[] for j in range(n)]

for i in range(m):
    b[a[i][0] - 1].append(a[i][1] - 1)
    b[a[i][1] - 1].append(a[i][0] - 1)


stm = 0
stv = 0
used = [0] * n
for i in range(n):
    if len(b[i]) > stm:
        stm = len(b[i])
        stv = i

ocher = [0] * 1000009
u = 0
k = 1
ocher[0] = stv


def bfs(x):
    nonlocal k
    for i in range(len(b[x])):
        if used[b[x][i]] == 0:
            print(x + 1, b[x][i] + 1)
            used[b[x][i]] = 1
            ocher[k] = b[x][i]
            k += 1



used[stv] = 1
while k - u > 0:
    bfs(ocher[u])
    u += 1


