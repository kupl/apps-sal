v, e = list(map(int, input().strip().split()))

edges = [[] for _ in range(v)]
for i in range(e):
    x, y = input().strip().split()
    x = int(x) - 1
    y = int(y) - 1
    edges[x].append(y)
    edges[y].append(x)


degreeTwo = [i for i in range(v) if len(edges[i]) == 2]

components = [-1] * v
numComp = 0

ans = 0

for x in degreeTwo:
    if components[x] == -1:
        flag = True
        queue = [x]
        while queue:
            curr = queue.pop(0)
            flag = flag and len(edges[curr]) == 2
            components[curr] = numComp
            for neigh in edges[curr]:
                if components[neigh] == -1:
                    queue.append(neigh)
                    components[neigh] = numComp
        numComp += 1
        ans += int(flag)

print(ans)

# components = [-1] * v

# numComp = 0

# for i in range(v):
# 	if components[i] == -1:
# 		queue = [i]
# 		while queue:
# 			curr = queue.pop(0)
# 			components[curr] = numComp
# 			for neigh in edges[curr]:
# 				if components[neigh] == -1:
# 					queue.append(neigh)
# 		numComp += 1

# c = [[] for _ in range(numComp)]

# for i in range(numComp):
# 	for j in range(v):
# 		if components[j] == i:
# 			c[i].append(j)

# ans = 0
# for comp in c:
# 	if len(comp) >= 3:
# 		flag = True
# 		for vertex in comp:
# 			if len(edges[vertex]) != 2:
# 				flag = False
# 				break
# 		if flag:
# 			ans += 1

# print(ans)
