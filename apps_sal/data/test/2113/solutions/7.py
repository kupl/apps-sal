import sys


def main():
    numNodes = [int(x) for x in sys.stdin.readline().rsplit()][0]
    adjList = {}
    nodeColors = {}
    unmarked = {}
    for i in range(1, numNodes + 1):
        adjList[i] = []
        unmarked[i] = True
    for line in sys.stdin.read().split('\n'):
        lineUnpacked = [int(x) for x in line.rsplit()]
        if len(lineUnpacked) < 2:
            continue
        (node1, node2) = lineUnpacked
        adjList[node1].append(node2)
        adjList[node2].append(node1)
    bfsList = []
    bfsList.append(1)
    nodeColors[1] = True
    unmarked[1] = False
    set1 = [1]
    set2 = []
    while len(bfsList) > 0:
        nodeConsidered = bfsList.pop(0)
        colorConsidered = nodeColors[nodeConsidered]
        newNodes = [x for x in adjList[nodeConsidered] if unmarked[x]]
        newNodes = list(newNodes)
        for node in newNodes:
            unmarked[node] = False
            nodeColors[node] = not colorConsidered
        bfsList.extend(newNodes)
        if colorConsidered:
            set2.extend(newNodes)
        else:
            set1.extend(newNodes)
    count = 0
    for node in set1:
        count = count + len(set2) - len(adjList[node])
    return count


print(main())
