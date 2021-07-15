import math
prime = [True for i in range(10**6+1)]
def SieveOfEratosthenes(n): 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True):
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1

def __starting_point():
	s = str(input())
	s1 =str(input())
	c = -10**9
	con = 0
	F = 0
	for i in range(0, len(s)):
		con = 0
		if len(s)-i>=len(s1):
			F = i
			for j in range(0, len(s1)):
				if s[F]==s1[j]:
					con+=1
				F+=1
		c=max(c,con)

	print((len(s1)-c))



__starting_point()
