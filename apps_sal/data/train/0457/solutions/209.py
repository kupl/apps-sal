import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        seen = set()
        queue = collections.deque()
        for coin in coins:
            queue.append((amount - coin, 1))
        
        while queue: 
            curr = queue.popleft()
            if curr[0] == 0: return curr[1]
            if curr[0] < 0 or curr[0] in seen: continue
            seen.add(curr[0])
            for coin in coins:
                queue.append((curr[0] - coin, curr[1] + 1))
        
        return -1
