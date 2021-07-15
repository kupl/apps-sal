n, m = map(int, input().split())

colors = {}

for i in range(m):
	a, b, c = map(int, input().split())
	if a not in colors and b not in colors and c not in colors:
		colors[a] = 1
		colors[b] = 2
		colors[c] = 3
	else:
		l = [1, 2, 3]
		if a in colors:
			l.remove(colors[a])
			colors[b], colors[c] = l[0], l[1]
		elif b in colors:
			l.remove(colors[b])
			colors[a], colors[c] = l[0], l[1]
		else:
			l.remove(colors[c])
			colors[a], colors[b] = l[0], l[1]

for i in colors:
	print(colors[i], end=' ')

