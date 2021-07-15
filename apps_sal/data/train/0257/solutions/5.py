class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        
        for (a, b), probability in zip(edges, succProb):
            graph[a].append([b, probability])
            graph[b].append([a, probability])
        
        if start == end:
            return 1
        
        queue = [[-1, start]]
        visited = set()
        distance_map = defaultdict(lambda: float('inf'))
        
        while queue:
            prob, node = heappop(queue)
            
            visited.add(node)
            
            if node == end:
                return -prob
            
            for neighbour, next_prob in graph[node]:
                if neighbour in visited:
                    continue
                heappush(queue, [prob * next_prob, neighbour])
        
        return 0
