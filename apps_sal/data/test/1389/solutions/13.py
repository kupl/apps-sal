n,m=map(int,input().strip().split())
s=[]
for i in range(n):
    s.append(input())
f=[[0 for i in range(m+1)] for j in range(n+1)]
ans=0
for k in range(n+m,1,-1):
    for i in range(n,0,-1):
        j=k-i
        if (j>m or j<1):
            continue
        #print(str(i)+" "+str(j)+s[i-1][j-1])
        tmp=0
        if (s[i-1][j-1]=='W'):
            tmp=1-f[i][j]
        else:
            tmp=-1-f[i][j]
        if (tmp!=0):
            ans=ans+1
            for x in range(1,i+1):
                for y in range(1,j+1):
                    f[x][y]=f[x][y]+tmp
print(ans)
