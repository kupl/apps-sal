import queue

n = int(input())
values = [ (int(value) - 1) for value in input().split() ]

start = 0

points = queue.Queue()
points.put(start)
d = [n*10] * n
d[start] = 0

while not points.empty():
	value = points.get()
	for destanation in [value - 1, value + 1, values[value]]:
		distance = d[value] + 1
		if destanation < 0 or destanation >= n:
			continue
		elif d[destanation] > distance:
			d[destanation] = distance
			points.put(destanation)

for value in d:
	print(value, end = ' ')

print('')

