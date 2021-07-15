t = int(input())
for gsdagsa in range(t):
	s = list(input())
	r = ''
	for i in range(len(s)-1):
		if i % 2 == 0:
			r += s[i]
	r += s[-1]
	print(r)
