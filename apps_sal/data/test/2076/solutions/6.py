q = int(input())
for fwefe in range(q):
	wyn = 0
	a,b,c = list(map(int,input().split()))
	while b > 0 and c > 1:
		b -= 1
		c -= 2
		wyn += 3
	while a > 0 and b > 1:
		a -= 1
		b -= 2
		wyn += 3
	print(wyn)
