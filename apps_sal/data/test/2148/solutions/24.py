import math

n, r = map(int, input().split())

disk_list = map(int, input().split())

t = [-1 * r for i in range(1001)]

result = []
for disk in disk_list:

	start = disk - r * 2
	if start < 0:
		start = 0

	end = disk + r * 2
	if end > 1000:
		end = 1000

	max_y = 0
	for i in range(start, end + 1):

		x1 = i
		y1 = t[i]

		x2 = disk

		#Calculate y2
		y2 = math.sqrt(4 * (r**2) - (abs(x1 - x2) ** 2)) + y1


		if y2 > max_y:
			max_y = y2

	t[disk] = max_y
	result.append(max_y)

for i in result:
    print(i, end=" ")

#print(t[:10])

