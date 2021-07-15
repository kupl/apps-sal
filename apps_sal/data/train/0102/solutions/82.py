lst = []
for i in range(1, 11):
	for j in range(1, 10):
		lst.append(int(str(j) * i))
lst.sort()
t = int(input())
for i in range(t):
	n = int(input())
	c = 0
	for j in lst:
		if n >= j:
			c += 1
		else:
			break
	print(c)
