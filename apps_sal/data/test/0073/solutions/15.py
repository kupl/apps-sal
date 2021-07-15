'''input
5 5 10 5 4
'''
c, v0, v1, a, l = list(map(int, input().split()))
p = 0
d = 0
while True:
	p += min(v1, v0 + a*d)
	d += 1
	if p >= c:
		print(d)
		break
	p -= l


