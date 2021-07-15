N = input()
N = int(N)
res = 0
graph = [["polycarp"]]
for i in range(N):
	data = input().split(' ')
	reposter = data[0].lower()
	reposted = data[2].lower()
	length = len(graph)
	for i in range(length):
		if reposted in graph[i]:
			if i < length-1:
				graph[i+1].append(reposter)
			else:
				graph.append([reposter])
print(len(graph))
