n = int(input())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

max = 1
for i in range(1, n//2 + 1):
	if gcd(i, n-i) == 1:
		max = i

print(max, n-max)
