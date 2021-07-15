import random, math
a, b = map(int, input().split())
r = 1
if b > a + 6:
	print(0)
else:
	for i in range(a + 1, b + 1):
		r *= i % 10
	print(r % 10)
