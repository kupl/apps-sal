'''input
4
0110
0101
00001000
0001000
'''
for test in range(int(input())):
	s = input()
	ans = 0
	for l in range(1, min(20, len(s))+1):
		p = 0
		for i in range(len(s)-l+1):
			if s[i]=='0':
				p += 1
				continue
			x = int(s[i:i+l], 2)
			if x>=l and (x-l)<=p:
				ans+=1
			p = 0
	print(ans)


