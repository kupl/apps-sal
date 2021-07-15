def gcd(a,b):
	if b==0:
		return a
	if a//b!=0:
		l.append(a//b)
	return gcd(b,a%b)

l=[]
t=["A","B"]
x,y=list(map(int,input().split()))
g=gcd(x,y)

l[-1]-=1
if g==1:
	if x>y:
		start=0
	else:
		start=1
	s=''
	for v in range(len(l)):
		s+=str(l[v])+t[(start+v)%2]
	print(s)


else:
	print('Impossible')

