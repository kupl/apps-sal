n=int(input())
s=[]
for i in range(n):
    a=int(input())
    s_i=[]
    for j in range(a):
        x,y=map(int,input().split())
        s_i.append([x-1,y])
    s.append(s_i)

ans=0
for i in range(2**n):
    honest=[0]*n
    skip=False #矛盾があるときTrue
    for j in range(n):
        if ((i>>j)&1): honest[j]=1
    for j in range(n):
        if honest[j]==1:
            for k in range(len(s[j])):
                if honest[s[j][k][0]]!=s[j][k][1]:
                    skip=True
                    break
    if skip: continue
    ans=max(ans,sum(honest))
print(ans)
