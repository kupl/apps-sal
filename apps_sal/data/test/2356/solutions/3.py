t = int(input())
for i in range(t):
	n = int(input())
	mas = list(map(int, input().split()))
	mas.sort()
	mas.reverse()
	print(*mas)

