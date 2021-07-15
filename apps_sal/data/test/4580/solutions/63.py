N=int(input())
a=list(map(int,input().strip().split()))

c=[0 for n in range(8)]
f=0
for n in range(N):
    tmp=a[n]//400
    if tmp>=8:
        f+=1
    else:
        if c[tmp]==0:
            c[tmp]+=1
MIN=max(sum(c),1)
MAX=sum(c)+f
print((str(MIN)+" "+str(MAX)))

