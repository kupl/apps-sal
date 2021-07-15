  
def countDivisors(n) : 
	cnt = 0
	for i in range(1, int(n**(0.5)) + 1) : 
		if (n % i == 0) : 
			if (n / i == i) : 
				cnt = cnt + 1
			else : 
				cnt = cnt + 2
	return cnt 


def gcd(a,b): 
	if (b == 0): 
		 return a 
	return gcd(b, a%b)

n=int(input())
l=list(map(int,input().split()))
if n==1:
	print(countDivisors(l[0]))
else:
	hcf=gcd(l[0],l[1])
	for i in range(2,n):
		hcf=gcd(hcf,l[i])
	print(countDivisors(hcf))

