t = int(input())
for q in range(t):
	n, m = list(map(int, input().split()))
	print(n * m // 2 + n * m % 2)

