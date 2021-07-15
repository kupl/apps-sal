'''input
4
'''
n = int(input())
l = [[False] * n]
for s in range(n):
	for e in range(s+1, n+1):
		for x in range(len(l)):
			if True not in l[x][s:e]:
				l[x][s:e] = [True] * (e-s)
				break
		else:
			l.append([False] * n)
			l[-1][s:e] = [True] * (e-s)
print(len(l))

