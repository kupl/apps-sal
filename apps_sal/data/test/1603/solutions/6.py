n=int(input())

L=list(map(int,input().split()))
S=list(L)
for i in range(1,n):
    S[i]+=S[i-1]

X=list(sorted(L))
for i in range(1,n):
    X[i]+=X[i-1]
q=int(input())

while(q):
    q-=1
    t,x,y=list(map(int,input().split()))
    if(t==1):
        ans=S[y-1]
        if(x>1):
            ans-=S[x-2]
    else:
        ans=X[y-1]
        if(x>1):
            ans-=X[x-2]
    print(ans)

