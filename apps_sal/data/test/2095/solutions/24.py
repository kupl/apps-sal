import sys

def solve():
	i, nGCars, GCars = 1, 0, []
	ignore = input()

	for line in sys.stdin:
		for c in line.split():
			r = int(c)
			if r == 1 or r == 3:
				break
		else:
			GCars.append(str(i))
			nGCars += 1
		i += 1

	print(nGCars)
	print(" ".join(GCars))

solve()

