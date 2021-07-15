def pairGCD(a, b):
	while a:
		a, b = b % a, a
	return b

def gcd(l):
	res = l[0]
	for x in l[1:]:
		res = pairGCD(res, x)
	return res

n = int(input())
l = [int(x) for x in input().split()]
print(gcd(l) * n)

