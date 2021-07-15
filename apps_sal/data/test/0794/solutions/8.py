n = int(input())

*l, = map(int, input().split())
if len(set(l)) - 1:
	l.sort()
	print(*l)
else:
	print(-1)
