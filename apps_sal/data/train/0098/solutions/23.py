import sys

def read():
	return sys.stdin.readline()

def main():
	q = int(read())
	for i in range(q):
		c, m, x = list(map(int, read().split()))
		if c <= m and c <= x:
			print(c)
		elif m <= c and m <= x:
			print(m)
		else:
			t = x
			c -= x
			m -= x
			q = min(m, c, (m + c) // 3)
			print(t + q)
	
def __starting_point():
	main()

__starting_point()
