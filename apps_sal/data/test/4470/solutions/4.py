def solve(n):
	c = 0
	if n == 1:
		return c
	while n != 1:
		if n%2 == 0:
			n //= 2
		elif n%3 == 0:
			n = 2*n//3
		elif n%5 == 0:
			n = 4*n//5
		else:
			return -1
		c += 1
	return c


for _ in range(int(input().strip())):
	n = int(input().strip())
	print(solve(n))


