kk=lambda:list(map(int,input().split()))
ll=lambda:list(kk())
def check(i,j):
	if 0 <= i < n and 0 <= j < n:
		if ls[i][j] == 0:
			ls[i][j] = 1
			return True
	return False

n = int(input())
ls = [None]*n
for i in range(n):
	ls[i] = [(1 if i == "#" else 0) for i in input()]
for i in range(n):
	for j in range(n):
		if ls[i][j] == 1: continue
		if check(i, j) and check(i+1, j) and check(i+2,j) and check(i+1, j+1) and check(i+1, j-1):
			pass
		else:
			print("NO")
			return
print("YES")

