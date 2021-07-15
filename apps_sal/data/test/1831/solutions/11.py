def clave(ent):
	return min(ent)
a=[int(i) for i in input().split()]
t=set(int(i) for i in input().split())
x=[]
for i in range(1,a[1]):
	x.append([int(i) for i in input().split()])
x.sort(key=clave)
while len(x):
	f=True
	for c in x:
		if (c[0] in t) + (c[1] in t)==1:
			f=False
			t.update(c)
			x.remove(c)
			break
	if f:
		print('no')		
		return
print('yes')

