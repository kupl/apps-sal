import sys
from collections import defaultdict
import queue

n = int(sys.stdin.readline())

graph = defaultdict(list)

X, Y = [[] for i in range(n)], [[] for i in range(n)]
atX, atY = defaultdict(list), defaultdict(list)

for i in range(n):
	a, b = map(int, sys.stdin.readline().split())
	a -= 1; b-= 1
	X[i] = a; Y[i] = b
	atX[X[i]].append(i)
	atY[Y[i]].append(i)

visX = set(); visY = set()
found = [False]*n

ans = n*(-1)
for root in range(n):
	if found[root]: continue
	usedX, usedY = set(), set()

	que = queue.Queue()
	que.put(root)
	found[root] = True
	usedX.add(X[root])
	usedY.add(Y[root])

	while not que.empty():
		cur = que.get()
		toVisit = []
		if X[cur] not in visX:
			visX.add(X[cur])
			for ele in atX[X[cur]]:
				toVisit.append(ele)
		if Y[cur] not in visY:
			visY.add(Y[cur])
			for ele in atY[Y[cur]]:
				toVisit.append(ele)

		for ele in toVisit:
			if found[ele]: continue
			found[ele] = True
			usedX.add(X[ele])
			usedY.add(Y[ele])
			que.put(ele)
	ans += len(usedX)*len(usedY)
print(ans)
