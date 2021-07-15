lim = int(input())
dx, dy = dict(), dict()
summ = 0
for i in range(0, lim):
	x, y =(int(j) for j in input().split())
	diagx = x+y
	diagy = x-y
	if diagx in dx:
		dx[diagx]+=1
	else:
		dx[diagx]=1
	if diagy in dy:
		dy[diagy]+=1
	else:
		dy[diagy]=1
for i in dx:
	summ+= dx[i]*(dx[i]-1)//2
for i in dy:
	summ+= dy[i]*(dy[i]-1)//2
print(summ)
