n = int(input())

chu = []
bs = []

mi = -1
count = 0

for _ in range(n):
	x,k = map(int, input().split())
	chu.append([x,k])

chu.sort()

for i in range(n):
	x = chu[i][0]
	k = chu[i][1]

	if x <= mi:
		mi = min(mi, k)
	else:
		count += 1
		mi = k

	#print(bs,chu)
print(count)
