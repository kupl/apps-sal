from heapq import heappush, heappop
def dijkstra(graph:list, node:int, start:int) -> list:
    # graph[node] = [(cost, to)]
    inf = float('inf')
    dist = [inf]*node

    dist[start] = 0
    heap = [(0,start)]
    while heap:
        cost,thisNode = heappop(heap)
        for NextCost,NextNode in graph[thisNode]:
            dist_cand = dist[thisNode]+NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap,(dist[NextNode],NextNode))
    return dist
K = int(input())
g = [[] for _ in range(K)]
for n in range(1,K+1):
    g[n%K] += [(1,(n+1)%K),(0,10*n%K)]

print(dijkstra(g,K,1)[0]+1)
