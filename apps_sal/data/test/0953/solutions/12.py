def dfs(i):
	ret = []
	if not used[i]:
		used[i] = True
		ret += [i]
	for j in range(n): 
		if a[i][j]==1 and not used[j]:
			ret.extend(dfs(j))
	return ret



n = int(input())
p = list(map(int,input().split()))
ans = p
a = [list(map(int,input())) for i in range(n)]
used = [False for i in range(n)]
for i in range(n):
	if not used[i]:
		temp = []
		idx = dfs(i)
		idx.sort()
		for j in idx:
			temp.append(p[j])
		temp.sort()
		for k,j in enumerate(idx):
			ans[j] = temp[k]

print(" ".join(list(map(str,p))))

