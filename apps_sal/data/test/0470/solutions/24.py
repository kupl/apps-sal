t = [int(x) for x in input().split(' ')]

t.sort()
c = 0
for i in t:
	if t.count(i) == 1: c += 1
	
if c == 5:
	print(sum(t))
	return

c = 0

m = []

for i in t:
	if t.count(i) == 2: m.append(2*i)
	if t.count(i) == 3: m.append(3*i)
	if t.count(i) == 4: m.append(3*i)
	if t.count(i) == 5: m.append(3*i)
	
print(sum(t) - max(m))

