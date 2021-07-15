n, m = map(int, input().split())

m1 = [list(map(int, input().split())) for _ in range(n)]
m2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
	for j in range(m):
		m1[i][j], m2[i][j] = max(m1[i][j], m2[i][j]), min(m1[i][j], m2[i][j])

def check(matrix):
	return all(all(y > x for x, y in zip(row, row[1:])) for row in matrix)

print("Possible" if check(m1) and check(m2) and check(list(map(list, zip(*m1)))) and check(list(map(list, zip(*m2)))) else "Impossible")
