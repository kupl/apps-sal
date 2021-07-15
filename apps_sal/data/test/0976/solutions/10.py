'''from math import *
int(input())
list(map(int,input().split()))'''
def main():
	n, x = list(map(int,input().split()))
	time = 0

	for _ in range(n):
		l, r = list(map(int,input().split()))
		if _ == 0:
			curr = 1
		time += (l - curr) % x + (r - l + 1)
		curr = r+1
	print(time)


def __starting_point():
	main()


__starting_point()
