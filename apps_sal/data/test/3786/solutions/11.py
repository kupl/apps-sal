n = int(input())

par = [None] + [int(i) - 1 for i in input().split()]
children = [[] for _ in range(n)]
for child in range(1, n):
    children[par[child]].append(child)

count = 0
nodesAtCurrLevel = [0]

while nodesAtCurrLevel:
    count += len(nodesAtCurrLevel) % 2
    
    nodesAtNextLevel = []
    for node in nodesAtCurrLevel:
        nodesAtNextLevel += children[node]
    
    nodesAtCurrLevel = nodesAtNextLevel

print(count)
