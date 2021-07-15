n,m=map(int, input().split())
s=[]
for i in range(m):
    tmp=list(map(int, input().split()))
    s.append(tmp[1:])
p=list(map(int, input().split()))
ans=0
for i in range(2**n):
    tmp=[0]*m
    for j in range(n):
        if ((i>>j) & 1):
            for k in range(m):
                if j+1 in s[k]:
                    tmp[k]+=1
    for t in range(m):
        if p[t]!=tmp[t]%2:
            break
    else:
        ans+=1
print(ans)
