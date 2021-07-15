for t in range(int(input())):
	n = int(input())
	tt = 1
	razr = 1
	c = 0
	while int(str(tt)*razr) <= n:
		c += 1
		tt += 1
		if tt == 10:
			tt = 1
			razr += 1
	print(c)
