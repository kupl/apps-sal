from collections import defaultdict
N, M, Q = list(map(int, input().split()))
l2r = defaultdict(int)
l2acc = [[0]*(N+1) for _ in range(N)]
r2acc = [[0]*(N+1) for _ in range(N)]
for _ in range(M):
    l, r = list(map(int, input().split()))
    l, r = l-1, r-1
    l2r[(l, r)] += 1
queries = []
for _ in range(Q):
    l, r = list(map(int, input().split()))
    l, r = l-1, r-1
    queries.append((l, r))

for l in range(N):
    acc = 0
    for r in range(l, N):
        acc += l2r[(l, r)]
        l2acc[l][r] = acc

for r in range(N):
    acc = 0
    for l in range(r, -1, -1):
        acc += l2acc[l][r]
        r2acc[l][r] =acc

for l, r in queries:
    print((r2acc[l][r]))


