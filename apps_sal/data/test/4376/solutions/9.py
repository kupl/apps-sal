from itertools import accumulate

def main():
	n, m = [int(_) for _ in input().split()]
	a = [int(_) for _ in input().split()]
	b = [int(_) for _ in input().split()]



	i = 0
	acc = 0
	for x in b:
		while acc + a[i] < x:
			acc += a[i]
			i += 1
		print(i + 1, x - acc)


def __starting_point():
	main()

__starting_point()
