N = int(input())
A = list(map(int,input().split()))
B = N*[0]

for n in range(N):
  if n%2==0:
    B[0]+=A[n]
  else:
    B[0]-=A[n]

for n in range(N):
  if n==0:
    pass
  elif 1<=n<=N-1:
    B[n] = 2*A[n-1]-B[n-1]
  else:
    B[n] = 2*A[n]-B[0]

print(*B)
