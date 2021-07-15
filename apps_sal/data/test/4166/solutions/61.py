n,m=map(int,input().split())

d={}
ind=[0]*n

for i in range(n):
    d[i+1]='*'

for j in range(m):
    s,c=map(int,input().split())

    if ind[s-1]==0:
        d[s]=c
        ind[s-1]=1
    else:
        if d[s]!=c:
            print(-1)
            return


ans=''

if n>=2:
    if d[1]==0:
        print(-1)
        return

for k in range(n):
    if k==0:
        if n>=2:
            if d[k+1]=='*':
                ans+='1'
            else:
                ans+=str(d[k+1])
        else:
            if d[k+1]=='*':
                ans+='0'
            else:
                ans+=str(d[k+1])
    else:
        if d[k+1]=='*':
            ans+='0'
        else:
            ans+=str(d[k+1])

print(ans)
