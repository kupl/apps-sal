n,x0,y0 = list(map(int,input().split()))
tr = []
for i in range(n):
	tr.append(list(map(int,input().split())))

a = []
ans = 0
for i in range(n):
	if tr[i][1]-y0 == 0:
		ang = "inf"
	else:
		ang = (tr[i][0]-x0)/(tr[i][1]-y0)
	if not ang in a:
		a.append(ang)
		ans += 1

print(ans)


