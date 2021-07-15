n,d = [int(x) for x in input().split(' ')]

m,c=0,0

for i in range(d):
	k = input()
	if k.count('1') == n:
		m = max(m,c)
		c = 0
		continue
	else:
		c += 1
	
m = max(m,c)
print(m)
