
def collecting(k):
	n = [k*2]*9
	for t in range(4):
		for c in input():
			if c != '.':
				i = int(c)-1
				n[i] -= 1
				if n[i] < 0:
					print('NO')
					return
	print('YES')
	return

def main():
	k = int(input())
	collecting(k)

def __starting_point():
	main()
__starting_point()
