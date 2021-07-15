N,M=map(int,input().split())
S=[0]*(N)
Q=[0]*(N)
for i in range(M):
    p,s=map(str,input().split())
    p=int(p)
    if  s=='AC':
        S[p-1]=1
    elif s=='WA' and S[p-1] ==0:
        Q[p-1]+=1
    else:
        pass
Q_com= [x * y for (x, y) in zip(S, Q)]
print (S.count(1),sum(Q_com))
