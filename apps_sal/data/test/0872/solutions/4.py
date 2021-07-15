input()

a = list(map(int, input().split()))

if len(set([x % 2 for x in a])) == 1:
	print(*a)
else:
	print(*sorted(a))
