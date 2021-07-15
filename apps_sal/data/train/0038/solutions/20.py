t = int(input())

for qwe in range(t):
	n, k1, k2 = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	if max(a) == n:
		print("YES")
	else:
		print("NO")
