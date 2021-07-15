k, x = map(int, input().split())

y = []

for i in range((x - (k - 1)), (x + k)):
	y.append(i)
print(' '.join(map(str, y)))
