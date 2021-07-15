N,M=list(map(int,input().split()))
X=list(map(int,input().split()))
Y=[]
X.sort()
ans=0
if N>=M:
    print((0))
    return
for i in range(M-1):
    Y.append(X[i+1]-X[i])
Y.sort(reverse=True)
for j in range(N-1):
    ans+=Y[j]-1

print((X[M-1]-X[0]+1-ans-N))

