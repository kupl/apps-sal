from math import gcd

n = int(input())
a = [int(i) for i in input().split()]
a.sort()
g = 0
for i in a:
	g = gcd(g, i - a[0])
print((a[-1] - a[0]) // g - n + 1)

