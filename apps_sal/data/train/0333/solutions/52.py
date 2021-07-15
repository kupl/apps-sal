class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)
        
        queue = [0]
        seen = {0}
        steps = 0
        while queue:
            next_ = []
            for node in queue:
                if node == n - 1:
                    return steps
                for neighbor in graph[arr[node]]:
                     
                    if neighbor not in seen:
                        seen.add(neighbor)
                        next_.append(neighbor)
                
                for neighbor in [node-1, node+1]:
    
                    if 0 <= neighbor < n and neighbor not in seen:
                        seen.add(neighbor)
                        next_.append(neighbor)
                graph[arr[node]].clear()        
                        
            queue = next_
            steps += 1
            
        return -1
