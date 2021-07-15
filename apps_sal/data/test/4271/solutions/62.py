N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
res = 0
for x in range(N-1):
  res += B[x]
  if A[x] + 1 == A[x+1]:
    res += C[A[x] - 1]
print(res + B[-1])
