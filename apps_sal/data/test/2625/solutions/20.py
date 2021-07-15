import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

for _ in range(iread()):
	k, x = viread()
	print(x + 9 * (k - 1))

