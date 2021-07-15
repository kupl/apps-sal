from sys import stdin,stdout

def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

n=int(stdin.readline())
a=[0]*n
for _ in range(n):
	a[_] = format(int(stdin.readline().strip(),16),"b").zfill(n)
	

r=[]
t= 1
for i in range(1,n):
	if a[i]==a[i-1]:
		t+=1
	else:
		r.append(t)
		t=1
r.append(t)

c=[]
t=1
for i in range(1,n):
	f=1
	for j in range(n):
		if a[j][i-1]!=a[j][i]:
			f=0
			break
	if f==1:
		t+=1
	else:
		c.append(t)
		t=1
c.append(t)

ans = r[0]
for i in r+c:
	ans = gcd(ans,i)

stdout.write("%d" %ans)

