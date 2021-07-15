n, m = map(int, input().split())
a = [tuple(map(int, input().split())) for i in range(n)]
b = [tuple(map(int, input().split())) for i in range(n)]
diff = [[a[i][j] ^ b[i][j] for j in range(m)] for i in range(n)]
for line in diff:
	if line.count(1) & 1:
		print('No')
		return
for j in range(m):
	if [diff[i][j] for i in range(n)].count(1) & 1:
		print('No')
		return
print('Yes')
