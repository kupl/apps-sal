k = int(input())
l = []
c=0
i=1
while c<=10000:
	if sum(list(map(int, str(i)))) == 10:
		l.append(i)
		c += 1
	i += 9
		
print(l[k-1])
