n = int(input())

a = []
b = []

for i in range(n):
	x,y = map(int,input().split())
	a.append(x)
	b.append(y)

if(n >= 2):
	total = 2
elif(n == 1):
	total = 1

p = a[0]

for i in range(1,n-1):
	c = a[i] - b[i]
	d = a[i]+b[i]
	if(c > 0 and c > p):
		p = a[i]
		total += 1
	elif(d < a[i+1]):
		p = d
		total += 1
	else:
		p = a[i]

print(total)
