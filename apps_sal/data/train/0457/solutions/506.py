class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        queue = [[0, 0]]
        visited = {0}
        num = 0
        for pos, num in queue:
            for c in coins:
                if pos + c in visited: continue
                if pos + c == amount: return num + 1
                if pos + c < amount:
                    queue.append([pos + c, num + 1])
                    visited.add(pos + c)
        return -1
        '''dp = [0] + [float('inf')] * amount
        
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1'''
