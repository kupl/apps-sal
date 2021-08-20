(N, M, Q) = map(int, input().split())
Trs = [tuple(map(int, input().split())) for i in range(M)]
pqs = [tuple(map(int, input().split())) for i in range(Q)]
cs = [[0 for i in range(N + 1)] for j in range(N + 1)]
for tr in Trs:
    cs[tr[0]][tr[1]] += 1
for i in range(N):
    for j in range(N):
        cs[i + 1][j + 1] += cs[i + 1][j]
for i in range(N):
    for j in range(N):
        cs[i + 1][j + 1] += cs[i][j + 1]
for pq in pqs:
    p = pq[0]
    q = pq[1]
    n = cs[q][q] - cs[q][p - 1] - cs[p - 1][q] + cs[p - 1][p - 1]
    print(n)
