n,m=list(map(int,input().split()))
a=[]
l=m+1
r=-1
u=n+1
d=-1
lma=m+1
rma=-1
uma=n+1
dma=-1
for i in range(n):
    a.append(input().strip())
    if a[i].find('*')!=-1:
        l=a[i].find('*')
        r=a[i].rfind('*')
    if l<lma:
        lma=l
    if r>rma:
        rma=r
    if '*' in a[i] and uma==n+1:
        uma=i
    if '*' in a[i] and uma!=n+1:
        dma=i
print(max(dma-uma+1, rma-lma+1))

