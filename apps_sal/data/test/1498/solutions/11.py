n,q=map(int,input().split())
s=[0]*(n+1)
ans = []
for i in range(q):
    t,k,d=map(int,input().split())
    sm=[]
    for j in range(1, n+1):
        if s[j] < t:
            sm.append(j)
            if len(sm)==k:break
    if len(sm)!=k:ans.append('-1')
    else:
        ans.append(str(sum(sm)))
        for j in sm: s[j]=d+t-1
print('\n'.join(ans))
