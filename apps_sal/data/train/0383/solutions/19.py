class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        nodes = len(graph)
        min_count = float('inf')
        min_node = 0
        for node in sorted(initial):
            visited = set()
            queue = deque()
            count = 0
            for i in initial:
                if i != node and i not in visited:
                    queue.append(i)
                    visited.add(i)
                    count += 1
                    while queue:
                        curr = queue.popleft()
                        for i, edge in enumerate(graph[curr]):
                            if edge == 1 and i != node and i not in visited:
                                queue.append(i)
                                visited.add(i)
                                count += 1
            if count < min_count:
                min_count = count
                min_node = node
        return min_node
            
        

