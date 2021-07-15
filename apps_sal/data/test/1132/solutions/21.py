def bus_topology(neigh):
	#check if exactly two nodes have 1 neighbor
	#check if all other nodes have 2 neighbors
	single_neighbors = 0
	for i in range(1, len(neigh)):
		if len(neigh[i]) == 1:
			single_neighbors += 1
		elif len(neigh[i]) > 2:
			return False
	
	if single_neighbors == 2:
		return True
	else:
		return False

def ring_topology(neigh):
	#check if all nodes have exactly two neighbors
	for i in range(1, len(neigh)):
		if len(neigh[i]) > 2:
			return False
	return True

def star_topology(neigh, n):
	#check if one node has n-1 neighbors
	#check if all nodes have 1 neighbor 
	centernode = 0
	for i in range(1, len(neigh)):
		if len(neigh[i]) == n-1:
			centernode += 1
		elif len(neigh[i]) != 1:
			return False

	if centernode == 1:
		return True
	else:
		return False

n,m = [int(x) for x in input().split()]
#nodes, edges
neighbors = [[] for x in range(n+1)]

for i in range(m):
	u,v = (int(x) for x in input().split())
	neighbors[u].append(v)
	neighbors[v].append(u)

#for i in range(len(neighbors)):
#	print(i, neighbors[i])

if bus_topology(neighbors):
	print("bus topology")
elif ring_topology(neighbors):
	print("ring topology")
elif star_topology(neighbors,n):
	print("star topology")
else:
	print("unknown topology")
