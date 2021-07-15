s = input() + "\0"

c = 0
lp = 0

for i, e in enumerate(s):
	#print(i, s[lp], e)
	if s[lp] != e:
		if (i - lp) % 2 == 0:
			c += 1
		lp = i



print(c)

