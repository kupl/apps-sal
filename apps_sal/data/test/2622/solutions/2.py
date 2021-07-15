n, m = list(map(int, input().strip().split(' ')))
L, M = [], []
for i in range(n):
  L.append(tuple(input().strip()))

for i in range(0, m):
  M.append(tuple(input().strip()))

k=0
row, col = [], []
for i in range(n-m+1):
	init, end = i, i+m
	row.append(hash(tuple(L[init:end])))
	
	D = []
	for j in range(0, m):
	  D.append(tuple(M[j][init:end]))
	col.append(hash(tuple(D)))

for ix in range(len(row)):
	k=0
	for jx in range(len(row)):
		if row[ix]==col[jx]:
			k=1
			break
	if k==1:
	  break

print(ix+1,end=' ')
print(jx+1)
