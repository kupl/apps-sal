n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
x = list(map(int,input().split()))
d = {}
for i in l:
	for j in x:
		d[(i,j)] = i*j

c = -9999999999999999999
for i in d:
	if(d[i] > c):
		c = d[i]
		y = i[0]

l.remove(y)
c = -9999999999999999999
for i in l:
	for j in x:
		c = max(c,i*j)
print(c)

