'''input
37 -100
'''
p = [(0, 0)]
a, b = 0, 0
c = 1
while c < 202:
	for i in range(c-1):
		a += 1
		p.append((a, b))
	p.append((a+1, b, "*"))
	a += 1
	for j in range(c-1):
		b += 1
		p.append((a, b))
	p.append((a, b+1, "*"))
	b += 1
	for k in range(c):
		a -= 1
		p.append((a, b))
	p.append((a-1, b, "*"))
	a -= 1
	for l in range(c):
		b -= 1
		p.append((a, b))
	p.append((a, b-1, "*"))
	b -= 1
	c += 2
x, y = list(map(int, input().split()))
if (x, y) in p:
	z = p.index((x, y))
elif (x, y, "*") in p:
	z = p.index((x, y, "*"))
t = 0
for w in p[:z]:
	if len(w) == 3:
		t += 1
print(t)










