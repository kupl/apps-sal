n = input().split()
old = []
new = []
for i in range(int(n[1])):
	old.append(list(input()))
for i in range(int(n[0])):
	new.append([])
	for j in range(int(n[1])):
		new[-1].append(old[j][i])
		new[-1].append(old[j][i])
	new.append(new[-1])
for i in new:
	print(''.join(i))
