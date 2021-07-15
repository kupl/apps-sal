class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0 
        seen = set()
        seen.add(0)
        queue = deque([0])
        count = 0 
        while queue: 
            if amount in queue: 
                return count
            currlen = len(queue)
            for i in range(currlen): 
                node = queue.popleft()
                for c in coins: 
                    if c + node not in seen and c + node <= amount: 
                        queue.append(c + node)
                        seen.add(c + node)
            count += 1
        return -1 
        
        

