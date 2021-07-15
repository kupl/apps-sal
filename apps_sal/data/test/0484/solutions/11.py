n, a, b = map(int, input().split(' '))
seals = []
for i in range(n): seals.append(list(map(int, input().split(' '))))

def canFit(rect, a, b):
	x1, x2 = max(a, b), min(a, b)
	y1, y2 = max(rect[0], rect[1]), min(rect[0], rect[1])
	return x1 >= y1 and x2 >= y2;

seals.sort(key = lambda x: -x[0]*x[1])
best = 0
#Rects not squares
for i in range(n):
	for j in range(i+1, n):
		first = [seals[i][0] + seals[j][0], max(seals[i][1], seals[j][1])]
		second = [seals[i][0] + seals[j][1], max(seals[i][1], seals[j][0])]
		third = [max(seals[i][0], seals[j][0]), seals[i][1] + seals[j][1]]
		fourth = [max(seals[i][0], seals[j][1]), seals[i][1] + seals[j][0]]
		if canFit(first, a, b) or canFit(second, a, b) or canFit(third, a, b) or canFit(fourth, a, b):
			best = max(best, seals[i][0]*seals[i][1] + seals[j][0]*seals[j][1])

print(best)
