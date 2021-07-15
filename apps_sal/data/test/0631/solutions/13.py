t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	arr = [int(j) for j in input().split()]
	if sum(arr) == m:
		print("YES")
	else:
		print("NO")
