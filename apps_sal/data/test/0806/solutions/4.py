import copy
import itertools
import string

###

def powmod(x, p, m):
	if p <= 0:
		return 1
	if p <= 1:
		return x%m
	return powmod(x*x%m, p//2, m) * (x%m)**(p%2) % m

###

def to_basex(num, x):
	while num > 0:
		yield num % x
		num //= x

def from_basex(it, x):
	ret = 0
	p = 1
	for d in it:
		ret += d*p
		p *= x
	return ret

###

M = 10**9+7

def core():
	n, l, r = (int(x) for x in input().split())
	# print(n, l, r)
	
	l0m3 = (l + 2)//3*3
	r0m3 = r//3*3
	c0m3 = (r0m3 - l0m3)//3 + 1
	c1m3 = c0m3-1 + (1 if l%3 == 1 else 0) + (1 if r%3 != 0 else 0)
	c2m3 = c0m3-1 + (1 if l%3 != 0 else 0) + (1 if r%3 == 2 else 0)
	
	# print(l0m3, r0m3, c0m3, c1m3, c2m3)
	
	dp = [[1], [0], [0]]
	for i in range(n):
		dp[0].append((dp[0][i]*c0m3 + dp[1][i]*c2m3 + dp[2][i]*c1m3) % M)
		dp[1].append((dp[0][i]*c1m3 + dp[1][i]*c0m3 + dp[2][i]*c2m3) % M)
		dp[2].append((dp[0][i]*c2m3 + dp[1][i]*c1m3 + dp[2][i]*c0m3) % M)
		
	# print(dp[0])
	# print(dp[1])
	# print(dp[2])
	
	ans = dp[0][-1]
	print(ans)


core()


































































































