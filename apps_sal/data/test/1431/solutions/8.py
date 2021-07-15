from copy import deepcopy

N=int(input())
A=list(map(int,input().split()))
ans=[0]*(N//2+1)+A[N//2:]
A=[0]+A

ok=1
for i in range(N//2,0,-1):
  if sum(ans[i*2:i*(N//i)+1:i])%2==0:
    ans[i]=A[i]
  else:
    ans[i]=1-A[i]

ans2=[]
for i in range(1,N+1):
  if ans[i]==1:
    ans2.append(i)

print(len(ans2))
if len(ans2)>0:print(*ans2)
