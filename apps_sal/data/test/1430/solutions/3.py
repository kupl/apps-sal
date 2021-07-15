from collections import *
n,k=map(int,input().split())
s=input()
q=deque()
tt=0
f=False
t=0
ans=0
tmp=0
for i in range(n):
    if f:
        if s[i]=="0":
            tmp+=1
            tt+=1
            if tmp>ans:
                ans=tmp
        else:
            q.append(tt)
            f=False
            tt=1
            tmp+=1
            if tmp>ans:
                ans=tmp

    elif f==False:
        if s[i]=="1":
            tmp+=1
            tt+=1
            if tmp>ans:
                ans=tmp
        else:
            t+=1
            f=True
            if t>k:
                d=q.popleft()
                tmp-=d
            tmp+=1
            tt+=1
print(ans)
