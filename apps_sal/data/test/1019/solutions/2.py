def gcd(a,b):
	return gcd(b,a%b) if a%b else b

n = int(input())
for i in range(n):
	num = n - i
	if(num < i):
		if(gcd(num,i) == 1):
			print(num,i)
			break
