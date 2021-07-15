from sys import stdin,stdout
def hexa(c):
	if c=='0':
		return "0000"
	if c=='1':
		return "0001"
	if c=='2':
		return "0010"
	if c=='3':
		return "0011"
	if c=='4':
		return "0100"
	if c=='5':
		return "0101"
	if c=='6':
		return "0110"
	if c=='7':
		return "0111"
	if c=='8':
		return "1000"
	if c=='9':
		return "1001"
	if c=='A':
		return "1010"
	if c=='B':
		return "1011"
	if c=='C':
		return "1100"
	if c=='D':
		return "1101"
	if c=='E':
		return "1110"
	if c=='F':
		return "1111"
#hexa = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

n=int(stdin.readline())
a=[0]*n
for _ in range(n):
	s = stdin.readline().strip()
	t=""
	for i in s:
		
		t+=hexa(i)
	a[_] = t

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

