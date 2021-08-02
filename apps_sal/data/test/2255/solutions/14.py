from collections import defaultdict
from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insertKey(self, k):
        heappush(self.heap, k)

    def extractMin(self):
        return heappop(self.heap)


heapObj = MinHeap()


graph = defaultdict(list)
n, m = map(int, input().split())
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
visited = [False] * (n)
# queue = []
heapObj.insertKey(0)
visited[0] = True
count = 0
while count != n:
    s = heapObj.extractMin()
    print(s + 1, end=" ")
    for i in graph[s]:
        if visited[i] == False:
            heapObj.insertKey(i)
            visited[i] = True
    count += 1
print()
