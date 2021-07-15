t=int(input())
for t in range(t):
	n=int(input())
	a=[int(x) for x in input().split(' ')]
	a.reverse()
	print(*a)
