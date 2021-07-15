from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque()
        queue.append((amount,0))
        visited = set()
        while queue:
            remainder, level = queue.popleft()
            for coin in coins:
                if remainder - coin == 0:
                    return level+1
                
                elif remainder - coin > 0 and (remainder - coin) not in visited:
                    queue.append((remainder - coin,level+1))
                    visited.add(remainder-coin)
        
        return -1 
