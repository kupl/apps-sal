from sys import stdin
n,m=list(map(int,stdin.readline().strip().split()))
s=[]
for i in range(n):
    s.append(list(map(int,stdin.readline().strip().split())))
b=[[0 for i in range(m)] for j in range(n)]
ans=[]
for i in range(n-1):
    for j in range(m-1):
        if s[i][j]==1 and s[i+1][j]==1 and s[i+1][j+1]==1 and s[i][j+1]==1:
            ans.append([i+1,j+1])
            b[i][j]=1
            b[i][j+1]=1
            b[i+1][j]=1
            b[i+1][j+1]=1
flag=True
for i in range(n):
    for j in range(m):
        if(s[i][j]!=b[i][j]):
            flag=False
            break
if flag:
    print(len(ans))
    for i in ans:
        print(*i)
else:
    print(-1)

