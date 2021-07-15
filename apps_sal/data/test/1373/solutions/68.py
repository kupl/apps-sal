N,K=list(map(int,input().split()))
b=0
c=0
ans=0

for i in range(0,K):
    b+=i
    c+=(N-i)
ans=c-b+1


for i in range(K,N+1):
    b+=i
    c+=N-i
    ans+=c-b+1

print((ans%(10**9+7)))
 

