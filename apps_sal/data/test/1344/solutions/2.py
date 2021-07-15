from sys import stdin, stderr, stdout, exit
from time import time


def main():
	n = int(stdin.readline())
	inp = (int(x) for x in stdin.readline().strip().split())
	l = int(2e9)
	dp = []
	for x in inp:
		if(x > l):
			dp.append(dp[-1] + 1)
		else:
			dp.append(1)
		l = x
	stdout.write(str(max(dp)))


def __starting_point():
	main()

__starting_point()
