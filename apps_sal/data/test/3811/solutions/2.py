import sys
import math
f=sys.stdin

def prime_factors(n):
	if n%2==0:
		return 2
	d=3
	sqrt=(n**0.5)+1
	while n>1:
		if n%d==0:
			return d
		d+=2
		if d>sqrt:
			return n

n=int(f.readline().rstrip('\r\n'))
gcd=0
for i in range(n):
	a,b=map(int,f.readline().rstrip('\r\n').split())
	tmp=max(a,b)%min(a,b)
	if tmp==0:
		gcd=math.gcd(gcd,max(a,b))
	else:
		gcd=math.gcd(gcd,a*b)

if gcd>1:
	if gcd<=10000000000:
		sys.stdout.write(str(prime_factors(gcd))+"\n")
	else:
		if (math.gcd(gcd,a)>1):
			sys.stdout.write(str(math.gcd(gcd,a))+"\n")
		else:
			sys.stdout.write(str(math.gcd(gcd,b))+'\n')
else:
	sys.stdout.write("-1\n")
