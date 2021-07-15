m=998244353
n,*d=map(int,open(0).read().split())
a=s=1
for v in d:a=a*v%m;s+=v-1
for i in range(s-n+2,s):a=a*i%m
print(a)
