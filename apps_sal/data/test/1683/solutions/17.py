mod=998244353
s=0
input()
d=[0]*11
def get(n,l,i):
	if l<i: return (n,(d[i]*11*(int(n)%mod))%mod)
	t=((int(n)%mod)*10)%mod
	n=n[:-(2*i-1)]+'0'+n[-(2*i-1):]
	return (n,(d[i]*(t+int(n)%mod)%mod)%mod)
l=input().split()
for i in l:
	d[len(i)]+=1
for i in l:
	n=i
	x=len(n)
	for j in range(1,11):
		n,tmp=get(n,x,j)
		s=(s+tmp)%mod
print(s)
