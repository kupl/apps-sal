class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        N = 100010
        dist = [2 for i in range(N)]
        seen = set()

        h = [-1 for i in range(N)]
        e = {}
        ne = {}
        w = {}
        idx = 0

        def add(a, b, c, idx):
            e[idx], w[idx] = b, c
            ne[idx] = h[a]
            h[a] = idx

        for edge, prob in zip(edges, succProb):
            add(edge[0], edge[1], prob, idx)
            idx += 1
            add(edge[1], edge[0], prob, idx)
            idx += 1

        def heap_dijkstra():
            dist[start] = 1
            heap = []
            heapq.heappush(heap, (-1, start))

            while heap:
                t = heapq.heappop(heap)
                vertex, distance = t[1], -t[0]
                if vertex in seen:
                    continue

                seen.add(vertex)

                i = h[vertex]
                while i != -1:
                    j = e[i]
                    if dist[j] == 2 or dist[j] < distance * w[i]:
                        dist[j] = distance * w[i]
                        heapq.heappush(heap, (-dist[j], j))

                    i = ne[i]
            return dist[end]

        '''
        graph = [[1e-6 for i in range(N)] for j in range(N)]

        for edge, prob in zip(edges, succProb):
            graph[edge[0]][edge[1]] = max(prob, graph[edge[0]][edge[1]])   
            graph[edge[1]][edge[0]] = max(prob, graph[edge[1]][edge[0]])            
        
        def dijkstra():
            dist[start] = 1
            
            for i in range(n):
                t = -1
                for j in range(n):
                    if not seen[j] and (t == -1 or dist[t] < dist[j]):
                        t = j
                
                seen[t] = True
                for j in range(n):
                    dist[j] = max(dist[j], dist[t] * graph[t][j])
            
            return dist[end]
        
        '''

        output = heap_dijkstra()

        if output == 2 or output < 1e-5:
            return 0.0
        else:
            return output
