N=int(input())
P=list(map(int,input().split()))
M=[i for i in range(1,N+1)]
ans=0

for i,j in zip(P,M):
    if i!=j:
        ans+=1

if ans==2 or ans==0:
    print("YES")
else:
    print("NO")
