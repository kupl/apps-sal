n,w=map(int,input().split())
kind=[[] for _ in range(4)]
for i in range(n):
    w_,v=map(int,input().split())
    if i==0:
        stan=w_
    kind[w_-stan].append(v)
for i in range(4):
    kind[i].sort(reverse=True)
    if len(kind[i])>=2:
        for j in range(len(kind[i])-1):
            kind[i][j+1]+=kind[i][j]
    kind[i]=[0]+kind[i]
ans=0
for i in range(len(kind[0])):
    for j in range(len(kind[1])):
        for k in range(len(kind[2])):
            for l in range(len(kind[3])):
                if stan*i+(stan+1)*j+(stan+2)*k+(stan+3)*l<=w:
                    ans=max(ans,kind[0][i]+kind[1][j]+kind[2][k]+kind[3][l])
print(ans)
