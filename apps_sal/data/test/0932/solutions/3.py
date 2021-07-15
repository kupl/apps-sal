

[M,N] = [int(s) for s in input().split()]
B = []
for i in range(M):
    row = [int(s) for s in input().split()]
    B.append(row)

A = [[1 for j in range(N)] for i in range(M)]
for i in range(M):
    for j in range(N):
        if B[i][j]==0:
            A[i] = [0 for j in range(N)]
            for k in range(M): A[k][j] = 0

B1 = [[0 for j in range(N)] for i in range(M)]
for i in range(M):
    for j in range(N):
        if A[i][j]==1:
            B1[i] = [1 for j in range(N)]
            for k in range(M): B1[k][j] = 1

if B!=B1:
    print("NO")
else:
    print("YES")
    for i in range(M):
        print(' '.join(map(str,A[i])))
    


