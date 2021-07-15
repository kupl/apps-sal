import random, math
from copy import deepcopy as dc

MAXX = 101
MAXY = 101


# Function to take input
def input_test():
	n, q, c = list(map(int, input().strip().split(" ")))
	st = [[[0 for i in range(MAXX)] for j in range(MAXY)] for k in range(c+1)]
	
	# Taking Input and marking the values in the 
	# Frequency array and the grid that the star is present
	for _ in range(n):
		x, y, s = list(map(int, input().strip().split(" ")))
		for t in range(c+1):
			st[t][x][y] += (s+t) % (c+1)

	for k in range(c + 1):
		for i in range(1,MAXX):
			for j in range(1,MAXY):
				st[k][i][j] = st[k][i][j] + st[k][i-1][j] + st[k][i][j-1] - st[k][i-1][j-1]
	

	comp = st
	# for i in comp:
	# 	for j in i:
	# 		print(j)
	# 	print("Done")

	# Taking the Queries
	for _ in range(q):
		t, x1, y1, x2, y2 = list(map(int, input().strip().split(" ")))
		# t = t % (c+1)
		t = t % (c+1)
		to_be_add = comp[t][x1-1][y1-1]
		tot = comp[t][x2][y2] - comp[t][x2][y1-1] - comp[t][x1-1][y2] + to_be_add
		print(tot)




# Function to check test my code
def test():
	pass


input_test()
# test()

