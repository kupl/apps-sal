n = int(input())
a = [int(x) for x in input().split()]
a.sort()
if sum(a) % n == 0:
	print(n)
else:
	print(n - 1)

