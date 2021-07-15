N,*X=map(int,input().split())
S=[input() for i in range(N)]
f=1
d={'AB':(0,1),'AC':(0,2),'BC':(1,2)}
x='ABC'
a=[]
for i in range(N):
    if X[d[S[i]][0]]==1 and X[d[S[i]][1]]==1 and X.count(0)==1 and i<N-1:
        if S[i][0] in S[i+1]:
            X[d[S[i]][0]]+=1
            X[d[S[i]][1]]-=1
            a.append(x[d[S[i]][0]])
        else:
            X[d[S[i]][0]]-=1
            X[d[S[i]][1]]+=1
            a.append(x[d[S[i]][1]])
    elif X[d[S[i]][0]]<X[d[S[i]][1]]:
        X[d[S[i]][0]]+=1
        X[d[S[i]][1]]-=1
        a.append(x[d[S[i]][0]])
    else:
        X[d[S[i]][0]]-=1
        X[d[S[i]][1]]+=1
        a.append(x[d[S[i]][1]])
    if -1 in X:
        f=0;break
print(['No','Yes'][f])
if f:print(*a,sep='\n')
