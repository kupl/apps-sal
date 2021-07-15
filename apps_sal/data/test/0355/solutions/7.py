import sys


#sys.stdin = open("input.txt")
#sys.stdout = open("output.txt", "w")

tbl = []
for i in range(8):
	tbl.append(input())

bestW = 10
bestB = 10
#print(tbl)

for i in range(8):
	for j in range(8):
		#print(i, j)
		if tbl[i][j] == 'W':
			ok = True
			for k in range(i):
				if tbl[k][j] != '.':
					ok = False
			if ok:
				bestW = min(bestW, i)
		elif tbl[i][j] == 'B':
			ok = True
			for k in range(8-i-1):
				if tbl[i + k + 1][j] != '.':
					ok = False
			if ok:
				bestB = min(bestB, 8 - i - 1)

#print(bestW, bestB)
if bestW <= bestB:
	print('A')
else:
	print('B')
