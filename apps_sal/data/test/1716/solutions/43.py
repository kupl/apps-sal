N, M, Q = map(int, input().split())

imos = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    l, r = map(int, input().split())
    imos[l][r] += 1


for l in range(N-1, -1, -1):
    for r in range(N+1):
        imos[l][r] += imos[l+1][r]

for r in range(1, N+1):
    for l in range(N+1):
        imos[l][r] += imos[l][r-1]


for _ in range(Q):
    p, q = map(int, input().split())
    print(imos[p][q])
