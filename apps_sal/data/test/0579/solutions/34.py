n,k=list(map(int,input().split()))
p=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=-10**18
flag=dict()
for i in range(n):
    if i in flag:
        continue
    cur=i
    accum=[]
    flag[cur]=0
    s=0
    while flag[cur]<2:
        cur=p[cur]-1
        s+=c[cur]
        accum.append(s)
        if cur not in flag:
            flag[cur]=0
        else:
            flag[cur]+=1
    l=len(accum)//2
    accum=[0]+accum
    #print(accum)
    for x in range(1,l+1):
        if accum[x+l-1]-accum[x-1]<=0 or k//l<1:
            ans=max(ans,max(accum[x:x+min(k,l)])-accum[x-1])
        else:
            a=max(accum[x:x+l-1])-accum[x-1]
            d=accum[x+l-1]-accum[x-1]
            if k%l!=0:
                b=max(accum[x:x+k%l])-accum[x-1]
                ans=max(ans,max(k//l*d,k//l*d+b,(k//l-1)*d+a))
            else:
                b=max(accum[x:x+l-1])-accum[x-1]
                ans=max(ans,max(k//l*d,(k//l-1)*d+a))
print(ans)

