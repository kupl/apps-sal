N = int(input())
A = list(map(int,input().split()))
D1 = []
D2 = []

D1.append(abs(A[0]))
D2.append(abs(A[1]))

for i in range(1,N):
  D1.append(abs(A[i]-A[i-1]))
D1.append(abs(A[N-1]))

for i in range(1,N-1):
  D2.append(abs(A[i+1]-A[i-1]))
D2.append(abs(A[N-2]))

S = sum(D1)

for i in range(N):
  print(S-D1[i]-D1[i+1]+D2[i])
