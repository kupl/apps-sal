import math
n=int(input())
if n==1:
	print(1)
	return
a=[]
for i in range(1,n+1,2):
	a.append(1)
b=[]
for i in range(2,n+1,2):
	b.append(i)
p=len(b)
k=2
#print(p,b)
while p>0:
	c=[]
	#print(c)
	for i in range(p):
		if b[i]%k==0 and b[i]%(k*2)!=0:
			#del c[i]
			a.append(k)
			p-=1
			#print(p)
		else:
			c.append(b[i])
	b=c[:]
	k=k*2
	#print(k,p,b)
#print(a)
p=a[-1]//2
a.pop()
q=p
for i in range(p,n+1):
	if i%p==0 and i>q:
		q=i
a.append(q)
#print(a)
for i in a:
	print(i,end=" ")
#a.append(math.gcd(b[0],b[1]))
#3a.append(max(b[0],b[1]))
#print(a)
	
		

