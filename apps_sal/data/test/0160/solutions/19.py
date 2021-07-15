def factor(N):
    arr=[]
    for i in range(1,int(N**0.5)+1):
        if(N%i==0):
            arr.append(i)
            if(N//i!=i):
                arr.append(N//i)
    return arr

n,k=map(int,input().split())
a=list(map(int,input().split()))
sum_=sum(a)

fac=sorted(factor(sum_),reverse=True)
ans=1
for x in fac:
    li=sorted(z%x for z in a)
    res=0
    cum=[0]*(n+1)
    for i in range(n):
        cum[i+1]=cum[i]+li[i]
    for i in range(1,n):
        l,r=cum[i],x*(n-i)-(cum[n]-cum[i])
        if l==r and r<=k:
            ans=max(ans,x)
print(ans)
