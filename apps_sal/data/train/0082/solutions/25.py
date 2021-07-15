for _ in range(int(input())):
	n = int(input())
	p = [*list(map(int, input().split()))][::-1]
	print(*p)

