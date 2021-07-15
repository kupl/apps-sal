N = int(input())
A = list(map(int,input().split()))

X = [0] * N

X[0] += sum(A) - 2 * sum(A[1::2])

for i in range(1,N):
  X[i] = (2 * A[i-1]) - X[i-1]
  
print(*X)
