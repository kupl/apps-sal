s = input()
inf = 0x3f3f3f3f

ans = []
for i in range(10):
	ans.append([-1]*10)
for i in range(10):
	for j in range(i, 10):
		dist = [0] * 10
		for k in range(10):
			dist[k]=[inf]*10
		for k in range(10):
			dist[k][(k+i)%10]=1
			dist[k][(k+j)%10]=1

		for k in range(10):
			for ii in range(10):
				for jj in range(10):
					dist[ii][jj] = min(dist[ii][jj],dist[ii][k]+dist[k][jj])
		
		p = 0
		cnt = 0
		for k in range(1, len(s)):
			if dist[p][ord(s[k])-48] == inf:
				ans[i][j]=ans[j][i]=-1
				break
			cnt += dist[p][ord(s[k])-48] - 1
			p = ord(s[k]) - 48
		else:
			ans[i][j]=ans[j][i]=cnt


for arr in ans:
	for a in arr:
		print(a, end=' ')

	print()


