from copy import deepcopy

n, m, q = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(m)]
pq = [list(map(int, input().split())) for _ in range(q)]

cnt = [[0] * (n + 1) for _ in range(n + 1)]
for l, r in lr:
    cnt[l][r] += 1

acc = deepcopy(cnt)
for i in range(n):
    for j in range(n):
        tmp = acc[i][j + 1] + acc[i + 1][j] - acc[i][j]
        acc[i + 1][j + 1] += tmp

for p, q in pq:
    p -= 1
    ans = acc[q][q] - acc[p][q] - acc[q][p] + acc[p][p]
    print(ans)
