n,*d=map(int,open(0).read().split())
s,r,m=sum(d),1,998244353
for v in d:r=r*v%m
for i in range(n-2):r=r*(s-n-i)%m
print(r)
