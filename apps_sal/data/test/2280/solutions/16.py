T = int(input())
for i in range(T):
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()
	print(min(len(a) - 2, max(a[-2] - 1, 0)))


