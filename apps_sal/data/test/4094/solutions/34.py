import sys

k = int(input())
r = 0


for i in range(1, k+10):
	r *= 10
	r += 7
	r %= k
	if r == 0:
		print(i)
		return

print('-1')
