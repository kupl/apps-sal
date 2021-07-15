n=int(input())
s=[]
for i in range(n):
    s.append(input())
r,cl=0,0
for i in range(n):
    c=0
    for j in range(n):
        if s[i][j]=='E':
            c=c+1
    r=max(r,c)
for i in range(n):
    c=0
    for j in range(n):
        if s[j][i]=='E':
            c=c+1
    cl=max(cl,c)
if r==n and cl==n:
    print(-1)
else:
    ans=[]
    if r!=n:
        for i in range(n):
            for j in range(n):
                if s[i][j]=='.':
                    ans.append([i+1,j+1])
                    break
    else:
        for i in range(n):
            for j in range(n):
                if s[j][i]=='.':
                    ans.append([j+1,i+1])
                    break
    for i in range(n):
        print(ans[i][0],ans[i][1])
