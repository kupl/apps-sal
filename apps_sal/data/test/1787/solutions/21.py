s=input()
n=len(s)
b=[]
a=[0]*n
MOD=10**9+7
if s[0]=='a':
	a[0]=1
if s[0]=='b':
	b.append(0)
for i in range(1,n):
	a[i]=a[i-1]
	if s[i]=='a':
		a[i]+=1
		if len(b)>0:
			p=b[-1]
			if p>0:
				a[i]+=a[p-1]
	elif s[i]=='b':
		b.append(i)
	a[i]%=MOD
print(a[n-1]%MOD)
		

