n,m,*c=map(int,open(0).read().split())
d={0:1}
r=s=0
for i in c:s+=i;x=d.get(s%m,0);r+=x;d[s%m]=x+1
print(r)
