N,M,Q = map(int,input().split())
l = [[0 for i in range(N)] for j in range(N)]
 
for _ in range(M):
    L,R = map(int,input().split())
    l[L-1][R-1] += 1
 
csum = [[0 for i in range(N+1)] for j in range(N+1)]
 
for i in range(1,N+1):
    for j in range(1,N+1):
        csum[i][j] = csum[i][j-1] + csum[i-1][j] - csum[i-1][j-1] + l[i-1][j-1]
 
for _ in range(Q):
    p,q = map(int,input().split())
    print(csum[q][q]-csum[q][p-1]-csum[p-1][q]+csum[p-1][p-1])
