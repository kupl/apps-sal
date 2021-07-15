3

(n, x1, y1, x2, y2) = tuple(map(int, input().split()))

flowers = []
for i in range(n):
	(x, y) = tuple(map(int, input().split()))
	dis1 = (x-x1)**2 + (y-y1)**2
	dis2 = (x-x2)**2 + (y-y2)**2
	flowers.append((dis1, dis2))

#for i in flowers:
#	print(str(i[2]) + " " + str(i[3]))

flowers = sorted(flowers)

dis = []
for i in range(n+1):
	left = flowers[:i]
	right = flowers[i:]
	if len(left) == 0:
		leftmax = 0
	else:
		leftmax = sorted(left)[-1][0]
	if len(right) == 0:
		rightmax = 0
	else:
		rightmax = sorted(right, key=lambda tup: tup[1])[-1][1]
	dis.append(leftmax + rightmax)

print(str(min(dis)))

