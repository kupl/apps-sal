ROW = 5
mtx = []
for i in range(ROW):
	mtx.append(input().split(' '))

flag=False
for x in range(ROW):
	for y in range(len(mtx[x])):
		if mtx[x][y] == '1':
			flag=True
			break
	if(flag):
		break
x += 1
y += 1

print( abs(x - 3) + abs(y - 3) )


