N,M,Q = map(int, input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l,r = map(int, input().split())
    matrix[l][r] += 1
accmatrix = [[0]*(N+1) for _ in range(N+1)]
for l in range(1,N+1):
    accmatrix[l] = [x+y for x,y in zip(accmatrix[l-1],matrix[l])]
for l in range(1,N+1):
    lis = accmatrix[l]
    for r in range(1,N+1):
        lis[r] += lis[r-1]

for _ in range(Q):
    p,q = map(int, input().split())
    ans = accmatrix[q][q] - accmatrix[p-1][q]- accmatrix[q][p-1] + accmatrix[p-1][p-1]
    print(ans)
