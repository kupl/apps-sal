# return a path from source to target as well as the
# bottleneck capacity of links in the path
def dfs(graph, capacity, source, target):
	fringe = []
	fringe.append(([source], 9999999)) # each element in fringe is a tuple (path, bottleneckCapacity)
	visited = set()

	while len(fringe) != 0:
		currPath, currBottleneck = fringe.pop()
		currNode = currPath[-1]

		# goal check
		if currNode == target:
			return (currPath, currBottleneck)

		if currNode not in visited:
			# expand it
			visited.add(currNode)
			for nextNode, capacity in zip(graph[currNode], capacities[currNode]):
				if nextNode not in visited and capacity > 0:
					nextPath = currPath + [nextNode]
					nextBottleNeck = min(capacity, currBottleneck)
					fringe.append((nextPath, nextBottleNeck))

	return (None, None)

# return the max flow from source to sink in graph
# capacities will be modified
def ford_fulkerson(graph, capacities, source, sink):
	total = 0 # toal flow
	while True:
		path, bottleneck = dfs(graph, capacities, source, sink)

		if path is None: break

		total += bottleneck
		# decrease capacity of each link in path by bottleneck
		# increase capacity of the inverted version of each link in path by bottleneck
		for i in range(len(path) - 1):
			u, v = path[i], path[i+1]
			indexOfVInGraphU = graph[u].index(v)
			capacities[u][indexOfVInGraphU] -= bottleneck
			indexOfUInGraphV = graph[v].index(u)
			capacities[v][indexOfUInGraphV] += bottleneck
			assert(capacities[u][indexOfVInGraphU] >= 0 and capacities[v][indexOfUInGraphV] >= 0)

	return total


n, m = [int(x) for x in input().split(" ")]
ais = [int(x) for x in input().split(" ")]
bis = [int(x) for x in input().split(" ")]
if sum(ais) != sum(bis):
	print("NO")
	return

graph = [[] for _ in range(2*n + 2)]
capacities = [[] for _ in range(2*n + 2)]
INF = 9999999

# add link from source to left column
for v in range(1, n+1):
	graph[0].append(v)
	capacities[0].append(ais[v-1])
# add link from right column to sink
for u in range(n+1, 2*n+1):
	graph[u].append(2*n+1)
	capacities[u].append(bis[u-n-1])
# for link from node i to node n + i b/t two columns
for u in range(1, n+1):
	graph[u].append(n+u)
	capacities[u].append(INF)

# add edges b/t two columns
for _ in range(m):
	u, v = [int(x) for x in input().split(" ")]
	# u -> v AND v -> u
	# change index: u -> n + v AND v -> n + u
	graph[u].append(n+v)
	capacities[u].append(INF)

	graph[v].append(n+u)
	capacities[v].append(INF)

# augment graph with imaginary links
for u in range(2*n+2):
	for v in graph[u]:
		if u not in graph[v]:
			# add imaginary link v -> u with capacity 0, if not present
			graph[v].append(u)
			capacities[v].append(0)


maxFlow = ford_fulkerson(graph, capacities, 0, 2*n+1)
if maxFlow < sum(ais):
	print("NO")
	return
else:
	print("YES")
	for u in range(1, n+1):
		for v in range(n+1, 2*n+1):
			try:
				# if u -> v present, which is equivalent to checking if v -> u is present
				# the flow = linkCapacity of v -> u
				indexOfUInGraphV = graph[v].index(u)
				print(capacities[v][indexOfUInGraphV], end=" ")
			except:
				print(0, end=" ")
		print()

