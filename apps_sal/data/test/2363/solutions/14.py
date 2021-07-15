from sys import stdin

N = int(stdin.readline())

for n in range(N):
	a, b = map(int, stdin.readline().split())

	a, b = min(a, b), max(a, b)

	ops = 0
	while a > 0:
		ops += b // a
		a, b = b % a, a

	print(ops)
