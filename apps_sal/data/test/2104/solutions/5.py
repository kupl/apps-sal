l, r = map(int, input().split())
print('YES')
while l < r:
	print(l, l + 1)
	l += 2
