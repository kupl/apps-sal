n,k = list(map(int,input().split(" ")))
degrees = [0] * n
neighbors = [list() for x in range(n)]
for i in range(n-1):
	first,second = list(map(int,input().split(" ")))
	degrees[first-1] += 1
	degrees[second-1] += 1
	neighbors[first-1] += [second]
	neighbors[second-1] += [first]

# start at a leaf
curr = 0
for i in range(n):
	if degrees[i] == 1:
		curr = i+1
		break
if curr == 0 or len(neighbors[curr-1]) == 0:
	print("No")
	return
curr = neighbors[curr-1][0]


def check(prev,parent,curr,level,degrees,neighbors,k):
	#print("curr: ",curr)
	#print("level: ",level)
	if level == 0:
		return len(parent) == 1 and degrees[curr-1] == 1,[]
	checked = []
	for neighbor in neighbors[curr-1]:
		#print("neighbor: ",neighbor)
		#print("checked: ",checked)
		#print("parent: ",parent)
		if len(prev) != 0 and prev[0] == neighbor:
			checked += [neighbor]
			continue
		if len(parent) != 0 and parent[0] == neighbor:
			continue
		result,garbage = check([],[curr],neighbor,level-1,degrees,neighbors,k)
		if result:
			checked += [neighbor]
		else:
			#print("adding the parent")
			if len(parent) == 0:
				parent += [neighbor]
			else:
				return False,[]
	if len(checked) > 2 and len(parent) == 0 and level == k:
		#print("first check")
		return True,[]
	elif len(checked) > 2 and len(parent) == 1 and level != k:
		#print("second check")
		return True,parent
	else:
		#print("len(checked): ",len(checked))
		#print("len(parent): ",len(parent))
		#print("level: ",level)
		#print("the end fail statement")
		return False,[]

prev = []
parent = []
counter = 1
while(counter <= k):
	result,parent = check(prev,[],curr,counter,degrees,neighbors,k)
	if not(result):
		print("No")
		return
	if counter == k:
		print("Yes")
		return
	prev = [curr]
	curr = parent[0]
	counter += 1

		



