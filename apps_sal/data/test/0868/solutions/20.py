
def __starting_point():
	n, = map(int, input().split())
	if n == 0:
		print(1)
	elif n % 4 == 0:
		print(6)
	elif n % 4 == 1:
		print(8)
	elif n % 4 == 2:
		print(4)
	else:
		print(2)
__starting_point()
