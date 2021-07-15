n = int(input())
parent = [None] * n
children = [[] for i in range(n)]
for i in range(1, n):
	p = int(input())
	p = p - 1
	parent[i] = p
	children[p].append(i)

leaf = {}		
for i in range(n):
	if len(children[i]) == 0:
		leaf[i] = True
	else:
		leaf[i] = False

for i in range(n):
	if leaf[i]:
		continue
	c = 0
	for j in children[i]:
		if leaf[j]:
			c = c + 1
	if c < 3:
		print("No")
		quit()

print("Yes")
