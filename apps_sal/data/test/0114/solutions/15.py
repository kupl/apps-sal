r, c = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(r)]
dup = [[0 for j in range(c)] for i in range(r)]
odp = []
for i in range(r - 1):
	for j in range(c - 1):
		if mat[i][j] == 1 and mat[i+1][j] == 1 and mat[i+1][j+1] == 1 and mat[i][j+1] == 1:
			odp.append([i,j])
			dup[i][j] = 1
			dup[i][j+1] = 1
			dup[i+1][j] = 1
			dup[i+1][j+1] = 1
if mat == dup:
	print(len(odp))
	for i in odp:
		print(i[0]+1, i[1]+1)
else:
	print(-1)
