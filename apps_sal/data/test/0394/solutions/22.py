def tr(s,k):
    a=0
    s1=[]
    for i in range(1,len(s)):
        s1.append(s[i]-s[i-1])
    t=True
    for j in range(1,len(s)):
        if s[j]!=s[j-1]+s1[(j-1)%k]:
            t=False
            break
    return t
from sys import stdin
n=int(stdin.readline().strip())
#n,m=map(int,stdin.readline().strip().split())
s=[0]+list(map(int,stdin.readline().strip().split()))
ans=[]
for i in range(1,n+1):
    if tr(s,i):
        ans.append(i)
print(len(ans))
print(*ans)

