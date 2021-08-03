from itertools import combinations

N, M, X = map(int, input().split())
C, A = [], []
for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = float('INF')
for i in range(1, N + 1):
    for li in combinations(list(range(N)), i):
        cost = 0
        skill = [0] * M
        for j in li:
            cost += C[j]
            for k in range(M):
                skill[k] += A[j][k]
        if all([s >= X for s in skill]):
            ans = min(ans, cost)
if ans == float('INF'):
    print(-1)
else:
    print(ans)
