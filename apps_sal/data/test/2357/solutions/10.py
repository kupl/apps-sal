q = int(input())
for rew in range(q):
	n = int(input())
	l = list(map(int,input().split()))
	if len(l) == 1:
		print(-1)
	else:
		poz = {}
		for i in range(n + 1):
			poz[i] = []
		for i in range(n):
			poz[l[i]].append(i)
		spr = [10000000] * (n+1)
		for i in range(n+1):
			k = len(poz[i])
			for j in range(1, k):
				spr[i] = min(spr[i], poz[i][j]-poz[i][j-1])
		if min(spr) == 10000000:
			print(-1)
		else:
			print(min(spr) + 1)

