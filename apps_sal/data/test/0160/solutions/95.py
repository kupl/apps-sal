from collections import deque
def isok(x):
    que=deque(sorted(z%x for z in a))
    res=0
    while que:
        l=que[0]
        if l==0:
            que.popleft()
            continue
        r=que[-1]
        if r==0:
            que.pop()
            continue
        d=min(l,x-r)
        que[0]-=d
        que[-1]=(que[-1]+d)%x
        res+=d
    return res
        

n,k=map(int,input().split())
a=list(map(int,input().split()))
sum_=sum(a)

fac=set()
for i in range(1,sum_+1):
    if i*i>sum_:
        break
    if sum_%i==0:
        fac.add(i)
        fac.add(sum_//i)

fac=sorted(fac,reverse=True)
ans=1
for x in fac:
    c=isok(x)
    if c<=k:
        ans=x
        break
print(ans)
