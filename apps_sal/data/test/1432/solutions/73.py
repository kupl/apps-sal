N = int(input())
*A, = list(map(int, input().split()))
B = [0] * N
for i in range(N):
    B[0] -= A[i] * (i%2*2-1)
for i in range(1, N):
    B[i] = A[i-1]*2 - B[i-1]
print((*B))

