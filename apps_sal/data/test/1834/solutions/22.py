3

n = int(input())
a = sorted([int(i) for i in input().split()])

i = 0
d = 1
s = n-1

while s >= 0:
	print(a[i], end=' ')
	i += d * s
	s -= 1
	d *= -1

