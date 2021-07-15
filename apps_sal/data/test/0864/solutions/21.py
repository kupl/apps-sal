n,m=list(map(int,input().split()))
s=list(map(int,input().split()))
d=dict()
for i in s:
    try:
        d[i]+=1
    except:
        d.update({i:1})
s1=[]
for i in d:
    s1.append(d[i])
s1.sort()
ans=0
for i in range(1, 101):
    t=s1.copy()
    x=0
    while len(t)>0 and x!=n:
        if t[-1]<i:
            t.pop()
        else:
            t[-1]-=i
            x+=1
    if x==n:
        ans=max(ans,i)
        
print(ans)

