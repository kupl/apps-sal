T = int(input())
for kse in range(T):
	n, x, y = map(int, input().split())
	R = x+y-1
	R = min(n, R)
	L = x+y-n+1
	L = max(1, L)
	L = min(L, n)
	print(L, R)
