n = int(input())
s1 = [int(x) for x in input().split()]
s1.pop(0)
s2 = [int(x) for x in input().split()]
s2.pop(0)
c = 0
chk = [[False for x in range(11)] for x in range(11)]
while(True):
	if(c > 1000):
		print(-1)
		return
	
	if(not s1 or not s2):
		print(c,1 if not s2 else 2)
		return
	else:
		chk[s1[0]][s2[0]] = True
		if(s1[0] > s2[0]):
			s1.append(s2[0])
			s1.append(s1[0])
			s1.pop(0)
			s2.pop(0)
		else:
			s2.append(s1[0])
			s2.append(s2[0])
			s1.pop(0)
			s2.pop(0)
		c += 1

