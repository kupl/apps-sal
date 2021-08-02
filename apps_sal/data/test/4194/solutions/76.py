N, M = map(int, input().split())
A = [int(i) for i in input().split()]
for i in range(M):
    N -= A[i]
if(N >= 0):
    print(N)
else:
    print(-1)
