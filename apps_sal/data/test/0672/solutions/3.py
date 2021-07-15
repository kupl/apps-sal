import itertools
import math

def main():
	a, b = list(map(int, input().split()))

	if a == b:
		print("infinity")
		return
	if a < b:
		print(0)
		return
	a -= b

	n = 0

	for i in range(1, math.ceil(math.sqrt(a))):
		if (a % i == 0):
			n += (i > b) + (a // i > b)

	if math.sqrt(a) % 1 == 0 and math.sqrt(a) > b:
		n += 1

	print(n)

def __starting_point():
	main()

__starting_point()
