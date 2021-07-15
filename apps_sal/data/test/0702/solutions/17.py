#codeforces1150B_live
gi = lambda : list(map(int,input().strip().split()))
n, = gi()
m = [list(input()) for e in range(n)]
for k in range(1,n-1):
	for j in range(1,n-1):
		if m[k-1][j] == m[k+1][j] == m[k][j-1] == m[k][j+1] == m[k][j] == ".":
			m[k-1][j] = m[k+1][j] = m[k][j-1] = m[k][j+1] = m[k][j] = "#"
for k in range(n):
	for j in range(n):
		if m[k][j] == ".":
			print("NO")
			return
print("YES")

