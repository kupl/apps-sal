N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [0]*N
for i in range(N):
    A[i] = [ int(j) for j in input().split() ]

cnt = 0
for i in range(N):
    pm = C
    for j in range(M):
        pm += A[i][j]*B[j]
    if pm > 0:
        cnt += 1

print(cnt)
