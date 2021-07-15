#def pr():
#	print()
#	for i in range(n):
#		for j in range(n):
#			print(map1[i][j], end = "")
#		print()
#	print()
#-----------------------------------------------
def check():
	f = True
	for i in range(n):
		for j in range(n):
			if map1[i][j] != map2[i][j]:
				f = False
				break
	if f:
		return True
	
	f = True
	for i in range(n):
		for j in range(n):
			if map1[i][j] != map2[n - 1 - i][j]:
				f = False
				break
	if f:
		return True
	
	f = True
	for i in range(n):
		for j in range(n):
			if map1[i][j] != map2[i][n - 1 - j]:
				f = False
				break
	if f:
		return True
	

def rotate():
	wk1=[]
	for i in range(n):
		wk1.append([])
		for j in range(n):
			wk1[i].append(map1[i][j])
	
	for i in range(n):
		for j in range(n):
			map1[i][j] = wk1[j][n - 1 - i]


n = int(input())
map1 = []
for i in range(n):
	st = input()
	map1.append([])
	for j in st:
		map1[i].append(j)

map2 = []
for i in range(n):
	st = input()
	map2.append([])
	for j in st:
		map2[i].append(j)


f = False
for k in range(4):
	if check():
		f = True
		break
	rotate()

if f:
	print("Yes")
else:
	print("No")

