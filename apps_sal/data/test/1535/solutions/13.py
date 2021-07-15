
def main():
	n, x0, y0 = map(int, input().split())
	c = set()
	for i in range(n):
		x, y = map(int, input().split())
		if x - x0 == 0:
			c.add('inf')
		else:
			c.add((y-y0)/(x-x0))
	print(len(c))

def __starting_point():
	main()
__starting_point()
