import itertools
import math

def main():
	a = int(input())
	b = int(input())
	c = int(input())
	print(max(a*b*c, a+b+c, a+b*c, a*b+c, a*(b+c), (a+b)*c))

def __starting_point():
	main()

__starting_point()
