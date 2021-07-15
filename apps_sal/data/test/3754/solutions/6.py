I=input
n=int(I())
*d,=map(int, I().split())
a=1
m=998244353
s=sum(d)
d.extend(range(s-2*n+3,s-n+1))
for i in d:a*=i;a%=m
print(a)
