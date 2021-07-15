from math import ceil

n, x, y = list(map(int, input().split()))

a = list(map(int, input().split()))

if x > y:
	print(n)

if x <= y:
	print(ceil(len(list([_ for _ in a if _ <= x])) / 2))

