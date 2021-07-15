A,B,K = list(map(int,input().split()))

A1 = A
A2 = min(A+K,B+1)
for i in range(A1,A2):
  print(i)

B1 = max(B-K+1,A+K)
B2 = B+1  
for i in range(B1,B2):
  print(i)

