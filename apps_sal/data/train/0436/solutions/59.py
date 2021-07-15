class Solution:
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        
        from collections import deque
        queue = deque([n])
        level = 0
        seen = set()
        
        while queue:
            if 0 in queue:
                break
            for _ in range(len(queue)):
                node = queue.popleft()
                if node not in seen:
                    seen.add(node)
                    
                if node % 2 == 0:
                    if (node - node // 2) not in seen:
                        queue.append(node - node // 2)
                
                if node % 3 == 0:
                    if (node - 2 * node // 3) not in seen:
                        queue.append(node - 2 * node // 3)
                
                if node - 1 not in seen:
                    queue.append(node - 1)
            level += 1

        return level 
            
        
        

