N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=0
li=[]

for i in range(N):
    li.append(V[i]-C[i])

for j in range(N):
    if li[j]>0:
        ans+=li[j]
print(ans)

