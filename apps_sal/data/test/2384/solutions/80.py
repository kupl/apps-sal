# F - Select Half
N = int(input())
A = list(map(int,input().split()))

if N%2==0:
    rec = [[0]*N for _ in range(2)]
    rec[0][0] = A[0]
    rec[1][1] = A[1]
    for i in range(2,N):
        rec[0][i] = rec[0][i-2]+A[i]
        rec[1][i] = max(rec[0][i-3],rec[1][i-2])+A[i]
    ans = max(rec[0][N-2],rec[1][N-1])
else:
    rec = [[0]*N for _ in range(3)]
    rec[0][0] = A[0]
    rec[1][1] = A[1]
    rec[0][2] = A[0]+A[2]
    rec[2][2] = A[2]
    for i in range(3,N):
        rec[0][i] = rec[0][i-2]+A[i]
        rec[1][i] = max(rec[0][i-3],rec[1][i-2])+A[i]
        rec[2][i] = max(rec[0][i-4],rec[1][i-3],rec[2][i-2])+A[i]
    ans = max(rec[0][N-3],rec[1][N-2],rec[2][N-1])
    
print(ans)
