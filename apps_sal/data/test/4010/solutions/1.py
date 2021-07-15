q = int(input())
for rwe in range(q):
	n = int(input())
	l = list(map(int,input().split()))
	dasie = False
	d = {}
	for i in range(n):
		d[l[i]] = []
	for i in range(n):
		d[l[i]].append(i)
	for elt in d:
		if len(d[elt]) > 2:
			dasie = True
			break
		if len(d[elt]) < 2:
			continue
		if len(d[elt]) == 2:
			if d[elt][0] != d[elt][1] - 1:
				dasie = True
	if dasie:
		print("YES")
	else:
		print("NO")
