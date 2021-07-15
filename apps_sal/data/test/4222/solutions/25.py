N,K=map(int,input().split())
C=[0]*(N+1)
#print(C)
for i in range(K):
  d=int(input())
  A= list(map(int, input().split()))
  for j in range(d):
    C[(A[j])]+=1

#print(C)
print(C.count(0)-1)
