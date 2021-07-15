n = input().strip()
M = 1000000007
l = len(n)

a = 0
b = 0
for i,c in enumerate(n[::-1]):
	c = int(c)
	p = l - 1 - i
	a += p * (p + 1) // 2 * c * pow(10, i, M)
	a += b * c
	a %= M
	b += (i+1) * pow(10, i, M)
	b %= M
print(a)

