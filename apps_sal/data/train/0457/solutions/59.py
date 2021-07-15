class Solution:
    def bfs(self, cur, coins):
        if cur == 0:
            return 0
        queue = [(0, cur)]
        visited = {}
        while queue:
            times, cur = heapq.heappop(queue)
            for c in coins:
                if c == cur:
                    return times +1
                if c < cur:
                    if cur-c not in visited:
                        heapq.heappush(queue, (times+1, cur- c))
                        visited[cur-c] = True
        return -1
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.bfs(amount, coins)
