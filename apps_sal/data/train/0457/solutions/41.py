class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        queue = collections.deque([(0,0)])
        seen = set()
        while queue:
            curAmount,step = queue.popleft()
            if curAmount == amount:
                return step
            for j in range(len(coins)):
                newAmount = curAmount+coins[j]
                if newAmount <= amount and newAmount not in seen:
                    seen.add(newAmount)
                    queue.append((newAmount,step+1))
                    
        return -1

