n, k = [int(x) for x in input().split()]
s = 0
for i in range(n):
	l, r = [int(x) for x in input().split()]
	s += r - l + 1
print((k - s % k) % k)

