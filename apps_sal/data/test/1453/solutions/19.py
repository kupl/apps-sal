from sys import stdin
n,m=list(map(int,stdin.readline().strip().split()))
s=list(map(int,stdin.readline().strip().split()))
s.sort()
a1=[0]

a2=[0]
a=[[0] for i in range(m)]
for i in range(n):

    a[i%m].append(s[i]+a[i%m][-1])
ans=[]
cnt=0
acum=0
for i in range(1,n+n):
    for j in range(m):
        cnt+=1
        acum+=a[j][i]
        ans.append(acum)
        if cnt==n:
            break
    if cnt==n:
        break
print(*ans)
        

