class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        Visited = {amount: 0}
        coins.sort(reverse = True)
        queue = deque()
        queue.append(amount)
        while queue:
            curr = queue.popleft()
            for coin in coins:
                if curr - coin >= 0 and curr - coin not in Visited:
                    queue.append(curr - coin)
                    Visited[curr - coin] = Visited[curr] + 1
                if 0 in Visited:
                    return Visited[0]
        return -1
                
        

