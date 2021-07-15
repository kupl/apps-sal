n = int(input())
d = []
for i in range(n - 1):
	d.append(int(input()))
m = {i:[] for i in range(1, n + 1)}
z = {i:0 for i in range(1, n + 1)}
for i in range(len(d)):
	m[d[i]].append(i + 2)
for i in m:
	if m[i] == []:
		z[i] = -1
for i in m:
	for j in m[i]:
		if z[j] == -1:
			z[i] += 1
f = True
for i in z:
	if z[i] < 3 and z[i] != -1:
		f = False
		break
if f:
	print('Yes')
else:
	print('No')
