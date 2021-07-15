n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[b[i]//a[i] for i in range(n)]
d=[b[i]%a[i] for i in range(n)]
while k:
    i=c.index(min(c))
    mi=min(k,a[i]-d[i])
    d[i]+=mi
    k-=mi
    c[i]+=d[i]//a[i]
    d[i]%=a[i]
print(min(c))
