n, v = map(int, input().split())
trees = [list(map(int, input().split())) for i in range(n)]
trees.sort()

mergedTrees = []
treeIndex = 0
currentDay = trees[treeIndex][0]
while treeIndex < len(trees):
	nbFruits = 0
	while treeIndex < len(trees) and trees[treeIndex][0] == currentDay:
		nbFruits += trees[treeIndex][1]
		treeIndex += 1
	mergedTrees.append([currentDay, nbFruits])
	if treeIndex < len(trees):
		currentDay = trees[treeIndex][0]

collected = 0
for treeIndex, tree in enumerate(mergedTrees):
	used = 0
	if treeIndex >= 1:
		lastTree = mergedTrees[treeIndex - 1]
		if lastTree[0] == tree[0] - 1:
			used = min(v, lastTree[1])

		collected += min(v, lastTree[1])


	nextUsed = min(tree[1], v - used)
	collected += nextUsed
	tree[1] -= nextUsed

if len(mergedTrees) > 0:
	lastTree = mergedTrees[len(mergedTrees) - 1]
	collected += min(v, lastTree[1])

print(collected)
