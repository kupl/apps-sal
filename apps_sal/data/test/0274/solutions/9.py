input()
br = input()
d = []
com = 0
hmax = 0
for i in range(len(br)):
	if br[i] == '[':
		d.append({
			'open': True,
			'com': com
		})
		com += 2
	else:
		com -= 2
		d.append({
			'open': False,
			'com': com
		})

	if com > hmax:
		hmax = com

hmax -= 1

a = [[] for j in range(hmax + 2)]
y = 0
x = 0
ap = True
for j in range(len(d)):

	if ap:
		for kek in range(len(a)):
			a[kek].append(' ')
	else:
		ap = True

	i = d[j]
	y = i['com'] // 2
	y0 = y
	a[y][x] = '+'
	for _ in range(hmax - i['com']):
		y += 1
		a[y][x] = '|'
	y += 1
	a[y][x] = '+'

	if i['open']:
		for kek in range(len(a)):
			a[kek].append(' ')
		ap = False
		a[y0][x + 1] = '-'
		a[y][x + 1] = '-'
	else:
		a[y0][x - 1] = '-'
		a[y][x - 1] = '-'
	try:
		if i['open'] and not d[j + 1]['open']:
			x += 3
			for kek in range(len(a)):
				for _ in range(3):
					a[kek].append(' ')
	except:
		pass

	x += 1

for i in a:
	print(*i, sep='')
