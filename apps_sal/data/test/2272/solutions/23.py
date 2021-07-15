def graphAdd(u, v, G):
	for a, b in G:
		if (a<u and u<b) or (a<v and v<b):
			connect(G, u, v, a, b)
		if (u<a and a<v) or (u<b and b<v):
			connect(G, a, b, u, v)

def connect(G, u, v, w, x):
	G[(u, v)][(w, x)] = 1

def queueSort(G, l, u, v):
	start = l[u-1]
	visited = dict()
	visited[start] = 1
	end = l[v-1]

	q = [start]

	while q != []:
		cur = q.pop(0)
		for a, b in G[cur]:
			if ((a, b) == end):
				return "YES"
			if ((a,b) not in visited):
				visited[(a,b)] = 1
				q.append((a,b))
	return "NO"

numTest = int(input())

G = dict()
l = list()

while(numTest>0):

	inputList= list(map(int, input().split()))
	a = inputList[0]
	b = inputList[1]
	c = inputList[2]

	if a == 1:
		G[(b, c)] = {}
		graphAdd(b, c, G)
		l.append((b,c))
	else:
		print(queueSort(G, l, b, c))

	numTest -= 1
