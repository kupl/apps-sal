import sys

def read():
	return sys.stdin.readline()

def main():
	n = int(read())
	a = list(map(int, read().split()))
	a.sort()
	k = 0
	used = [0] * n
	for i in range(n):
		if used[i]:
			continue
		k += 1
		for j in range(i, n):
			if a[j] % a[i] == 0:
				used[j] = True
	print(k)
	
def __starting_point():
	main()

__starting_point()
