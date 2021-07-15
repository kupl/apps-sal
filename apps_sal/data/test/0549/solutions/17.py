import math

size = int(input())

sml = 1

for i in range(math.floor(math.sqrt(size)), 1, -1):
	if size % i == 0:
		sml = i
		break

print("{0} {1}".format(sml, size//sml))
