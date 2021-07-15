N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = []
C = []
for i in range(Q):
  B_temp,C_temp = map(int,input().split())
  B.append(B_temp)
  C.append(C_temp)
Counts = [0]*100010
for i in range(N):
  Counts[A[i]]=Counts[A[i]]+1

sum_A = 0
for i in range(100010):
  sum_A = sum_A + i*Counts[i]
  
for i in range(Q):
  sum_A = sum_A + Counts[B[i]]*(C[i]-B[i])
  Counts[C[i]] = Counts[C[i]]+Counts[B[i]]
  Counts[B[i]] = 0
  print(sum_A)
