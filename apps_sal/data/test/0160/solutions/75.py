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
        
def factor(N):
    arr=[]
    for i in range(1,int(N**0.5)+1):
        if(N%i==0):
            arr.append(i)
            if(N//i!=i):
                arr.append(N//i)
    return arr

n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
sum_=sum(a)

fac=sorted(factor(sum_),reverse=True)
ans=1
for x in fac:
    c=isok(x)
    if c<=k:
        ans=x
        break
print(ans)

