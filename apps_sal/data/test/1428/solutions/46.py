from collections import defaultdict
import itertools

n, c = list(map(int, input().split()))

D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]

d = [defaultdict(int), defaultdict(int), defaultdict(int)]

for i in range(n):
    for j in range(n):
        r = (i + j) % 3
        d[r][C[i][j]] += 1

cost = [[0] * c for _ in range(3)]

for i in range(3):
    dic = d[i]
    for j in range(c):
        for k, v in list(dic.items()):
            cost[i][j-1] += v * D[k-1][j-1]

ans = 1e9

for i, j, k in itertools.permutations(list(range(c)), 3):
    ans = min(cost[0][i] + cost[1][j] + cost[2][k], ans)

print(ans)



