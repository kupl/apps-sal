N = int(input())
A = list(map(int, input().split()))

S = sum(A)
X = [0]*N
X[0] = S-2*sum(A[1:N:2])
for i in range(1, N):
    X[i] = 2*A[i-1]-X[i-1]
print((*X))

