n = int(input())
a = list(map(int, input().split()))

c = 0
s = sum(a)
if s/n >= 4.5:
	print (c)
else:
	a.sort()
	for i in range(len(a)):
		c+=1
		s+=(5-a[i])
		a[i] = 5
		if (s/n>=4.5):
			break
	print (c)

