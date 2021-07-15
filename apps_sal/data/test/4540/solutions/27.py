N=int(input())
A=list(map(int,input().split()))
A.append(0)
sum=0
for i in range(N+1):
  if i==0:
    sum+=abs(A[0])
  else:
    sum+=abs(A[i-1]-A[i])
for i in range(N):
  if i==0:
    print(sum+(abs(A[1])-abs(A[1]-A[0])-abs(A[0])))
  else:
    print(sum+(abs(A[i+1]-A[i-1])-abs(A[i+1]-A[i])-abs(A[i]-A[i-1])))
