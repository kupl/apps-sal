q = int(input())
for iwer in range(q):
	c, kids = map(int,input().split())
	dystr = (c//kids)*kids
	cc = c
	c -= dystr
	poz = max(0, c - kids//2)
	print(cc-poz)
