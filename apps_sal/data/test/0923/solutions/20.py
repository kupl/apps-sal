def changeGear(x,i,n):
	if(i&1 == 0):
		if(x != n-1):
			return x + 1
		else:
			return 0
	else:
		if(x == 0):
			return n-1
		else:
			return x - 1

n = int(input())

a = list(map(int,input().split()))

b = []
c = []

for i in range(n):
	b.append(i)
	c.append(a[i])

if(a == b):
	print('Yes')
	return
else:
	for i in range(n):
		a[i] = changeGear(a[i],i,n)
#print(a)

while(a != b and a != c):
	for i in range(n):
		a[i] = changeGear(a[i],i,n)
	#print(a)

if(a == b):
	print('Yes')
else:
	print('No')
