m=998244353
n,*d=map(int,open(0).read().split())
a=s=1
for v in d:a=a*v%m;s+=v-1
while n-2:a=a*(s+2-n)%m;n-=1
print(a)
