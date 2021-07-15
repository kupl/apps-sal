m, n = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for i in range(m)]
c = 0
x, y = 0, 0
dupa  = 1
for i in range(m):
	if dupa == 0:
		break
	cur = matrix[i][0]
	for j in range(n):
		if matrix[i][j] != cur:
			x = i
			y = j
			print("TAK")
			c = 1
			dupa = 0
			break
import sys
if c == 0:
	zor = 0
	for i in range(m):
		zor = (zor^matrix[i][0])
	if zor == 0:
		print("NIE")
		return
	else:
		print("TAK")
		for k in range(m):
			print(1, end = " ")
		return
else:
	for i in range(m):
		if i != x:
			print(1, end = " ")
		else:
			a = matrix[x][y]
			b = matrix[x][0]
			sor = 0
			for g in range(m):
				sor = (sor^matrix[g][0])
			if sor > 0:
				print(0+1, end = " ")
			else:
				print(y + 1, end =  " ")
