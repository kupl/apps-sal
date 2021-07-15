class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # bfs only when prob is less than cur best add to the queue
        graph = [[] for _ in range(n)]
        for edge, p in zip(edges, succProb):
            a, b = edge
            graph[a].append((b, p))
            graph[b].append((a, p))
        prob = {start: 1}
        queue = [(start, 1)]
        while queue:
            new_queue = []
            for a, p_a in queue:
                for b, p_b in graph[a]:
                    p = p_a*p_b
                    if b not in prob or p > prob[b]:
                        prob[b] = p
                        new_queue.append((b, p))
            # print(prob)
            queue = new_queue
        return prob.get(end, 0)
