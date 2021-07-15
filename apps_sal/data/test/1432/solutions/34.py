N = int(input())
A = [int(x) for x in input().split()]
x = [0]*N
for i in range(N):
  x[0] += ((-1)**i)*A[i]
for i in range(1,N):
  x[i] = -x[i-1]+2*A[i-1]
for i in range(N):
  print(x[i],end=" ")
print()
