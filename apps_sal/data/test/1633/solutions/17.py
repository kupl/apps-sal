n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1,k+1):
	a, b = map(int, input().split())
	a = a - 1
	b = b - 1
	if arr[a][b] == 0: 
		arr[a][b] = i

ans = 100000000000
for i in range(n-1):
	for j in range(m-1):
		if arr[i][j] > 0 and arr[i+1][j] > 0 and arr[i][j+1] > 0 and arr[i+1][j+1] > 0:
			maxval = max(arr[i][j], max(arr[i][j+1], max(arr[i+1][j], arr[i+1][j+1])))
			ans = min(ans, maxval)

print(ans if ans != 100000000000 else 0)
