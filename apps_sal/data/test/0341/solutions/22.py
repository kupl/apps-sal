N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()+'*'*K
h=['']*N
f,n='',''
ans=0
for i in range(N):
    if K<=i:f=h[i-K]
    n=T[i+K]
    if T[i]=='r':
        if f=='p':h[i]=n
        else:ans+=P;h[i]='p'
    if T[i]=='p':
        if f=='s':h[i]=n
        else:ans+=S;h[i]='s'
    if T[i]=='s':
        if f=='r':h[i]=n
        else:ans+=R;h[i]='r'
print(ans)
