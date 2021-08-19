(n, m, q) = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(m)]
pq = [list(map(int, input().split())) for i in range(q)]
li = [[0] * (n + 1) for i in range(n + 1)]
for i in lr:
    (l, r) = (i[0], i[1])
    li[l][r] += 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        li[i][j] += li[i - 1][j] + li[i][j - 1] - li[i - 1][j - 1]
for i in pq:
    (p, q) = (i[0], i[1])
    print(li[q][q] - li[p - 1][q] - li[q][p - 1] + li[p - 1][p - 1])
