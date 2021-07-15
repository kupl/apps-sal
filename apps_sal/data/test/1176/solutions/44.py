N=int(input())
A=list(map(int,input().split()))
import bisect
A.sort()
B=[abs(i) for i in A]
l=min(B)
count=0
for i in range(N):
  if A[i]<0:
    count+=1
  else:
    break
if count%2==1:
  for i in range(count-1):
    A[i]=-A[i]

  print(sum(A)-2*l-2*A[count-1])

if count%2==0:
  for i in range(count):
    A[i]=-A[i]
  print(sum(A))
