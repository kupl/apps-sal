from numpy import *
A = (10**5+1)*[1]
B = (10**5+1)*[0]

for i in range(2,int(10**2.5)+1):
  if A[i]==1:
    for j in range(2*i,10**5+1,i):
      A[j] = 0

for n in range(3,10**5+1):
  if A[n] and A[(n+1)//2]:
    B[n]+=1

B = cumsum(B)
for q in range(int(input())):
  l,r = map(int,input().split())
  print(B[r]-B[l-1])
