import sys
n,m = list(map(int,sys.stdin.readline().rstrip().split()))
matrix = []
for _ in range(n):
	row = list(map(int,sys.stdin.readline().rstrip().split()))
	matrix.append(row)

# initialize table
A = [[1 for _ in range(m)] for _ in range(n)]
for i in range(n-2,-1,-1):
	for j in range(m):
		if matrix[i][j] <= matrix[i+1][j]:
			A[i][j] = A[i+1][j] + 1

# rows = [0] * n
# for i in range(n):
# 	lst = [A[i][j] for j in range(m)]
# 	rows[i] = max(lst)
rows = [max(row) for row in A]

ans = ""
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
	l,r = list(map(int,sys.stdin.readline().rstrip().split()))
	if rows[l-1] >= (r - l + 1):
		ans += "Yes\n"
	else:
		ans += "No\n"
sys.stdout.write(ans)

