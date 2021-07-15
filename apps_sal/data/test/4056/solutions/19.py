import math

def find_gcd(x, y): 
	
	while(y): 
		x, y = y, x % y 
	
	return x 
 
def calcDivisors(n) : 
	ans=0
	i = 1
	while i <= math.sqrt(n): 
		
		if (n % i == 0) : 
			 
			if (n / i == i) : 
				ans=ans+1
			else : 
				ans=ans+2 
		i = i + 1
	return ans	


			 
n=int(input())			 
l = [int(i) for i in input().split()] 

if n!=1:
	gcd = find_gcd(l[0], l[1])
if n==1:
	gcd=l[0] 

for i in range(2, n): 
	gcd = find_gcd(gcd, l[i]) 
	
print(calcDivisors(gcd)) 

