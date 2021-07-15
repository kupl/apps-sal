N,K=map(int,input().split())
X=list(map(int,input().split()))
for i in range(N):
    if X[i]<0:
        continue
    elif X[i]==0:
        K-=1
        if i<K:
            mX=[0]+[-x for x in X[:i]][::-1]
        else:
            mX=[0]+[-x for x in X[i-K:i]][::-1]
        pX=[0]+X[i+1:i+1+K]
        break
    else:
        if i<K:
            mX=[0]+[-x for x in X[:i]][::-1]
        else:
            mX=[0]+[-x for x in X[i-K:i]][::-1]
        pX=[0]+X[i:i+K]
        break
else:
    mX=[0]+[-x for x in X[::-1]]
    pX=[0]
ans=10**9
l=K-(len(pX)-1)
n=len(mX)
for i in range(len(pX)-1,-1,-1):
    if l<n:
        ans=min(ans,pX[i]+mX[l]*2,pX[i]*2+mX[l])
    else:
        break
    l+=1
print(ans)
