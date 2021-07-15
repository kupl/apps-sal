m, d = list(map(int, input().split()))

nd = [0,31,28,31,30,31,30,31,31,30,31,30,31][m]

nc = 0

nd = nd - (8 - d)
nc = nc + 1

while (nd > 0):
	nd = nd - 7
	nc = nc + 1

print(nc)


