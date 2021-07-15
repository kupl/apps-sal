N = int(input())
A = [a for a in range(2, N+1)]
T = 1
while len(A)>0:
  X = A[0]
  T *= sum(N//(X**i) for i in range(1, 11))+1
  A = [a for a in A if a%A[0]]
print(T%(10**9+7))
