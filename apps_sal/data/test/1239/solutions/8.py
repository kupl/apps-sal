input()
a = sorted([int(i) for i in input().split()])
best = float('inf')
quantity = 0
for i in range(1, len(a)):
	diff = abs(a[i] - a[i - 1])
	if diff == best:
		quantity += 1
	elif diff < best: 
		quantity = 1
		best = diff
print(best, quantity)

