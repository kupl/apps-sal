def try_t(i, j):
	if i < 0 or i >= n or j < 0 or j >= n:
		return False
	if A[i][j] == "#":
		return False
	A[i][j] = "#"
	return True

n = int(input())

A = []
for i in range(n):
	s = input()
	B = []
	for elem in s:
		B.append(elem)
	A.append(B)
T = True
for i in range(n):
	for j in range(n):
		if A[i][j] == '.':
			a1 = try_t(i + 1, j)
			a2 = try_t(i + 2, j)
			a3 = try_t(i + 1, j + 1)
			a4 = try_t(i + 1, j - 1)
			if not(a1 and a2 and a3 and a4):
				T = False
				break
if T:
	print("YES")
else:
	print("NO")
