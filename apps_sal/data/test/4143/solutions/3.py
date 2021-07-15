import math

N=int(input())
A=[int(input()) for _ in range(5)]
n=min(A)
for i in range(5):
  if n==A[i]:
    p=i
    break
k=math.ceil(N/n)
print(k+4)
