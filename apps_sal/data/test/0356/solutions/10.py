import sys
f=sys.stdin
out=sys.stdout

n=int(f.readline().rstrip('\r\n'))
a=list(map(int,f.readline().rstrip('\r\n').split()))
m=int(f.readline().rstrip('\r\n'))
b=list(map(int,f.readline().rstrip('\r\n').split()))

i=n-1
j=m-1
c=0
while i>=0 and j>=0:
	if a[i]==b[j]:
		c+=1
		i-=1
		j-=1
	elif a[i]<b[j]:
		a[i-1]+=a[i]
		i-=1
	else:
		b[j-1]+=b[j]
		j-=1
if i==-1 and j==-1:
	out.write(str(c))
else:
	out.write("-1")
