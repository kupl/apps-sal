import math as m

a, b = map(int, input().split())
if a > b:
	a, b = b, a
x = b - a
ans = int(5e18)
output = 0

G = 1
while G*G <= x:
	if x % G == 0:
		g = G
		k = (g - (a%g))%g
		res = (a + k) * (b + k) // m.gcd(a + k, b + k)
		if(res < ans):
			ans = res
			output = k
		elif res == ans:
			output = min(output, k)
		g = x // G
		k = (g - (a%g))%g
		res = (a + k) * (b + k) // m.gcd(a + k, b + k)
		if(res < ans):
			ans = res
			output = k
		elif res == ans:
			output = min(output, k)
	G += 1

print(output)
