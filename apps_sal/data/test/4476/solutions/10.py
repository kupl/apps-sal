t = int(input())
for iii in range(t):
	a, b = list(map(int, input().split()))
	tmp = b - a
	if tmp == 0:
		print(0)
	elif (a < b and tmp % 2 == 1) or (a > b and tmp % 2 == 0):
		print(1)
	else:
		print(2)

