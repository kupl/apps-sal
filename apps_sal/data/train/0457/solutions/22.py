'''
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

remain =11
fewest =inf
initially visited = (), q = [(11,1)] --count is 1 because of off-by-one (see code below)

after first while-iteration:
    q [(10,1),(9,1),(6,1)]
    visited(10,9,6)
    
----ALGO-----
BFS:
q = [(remain,count),(remain,count),...]
visited =set(amount_explored/to_explore, amt2, amt3) 
^ purpose: so we won't try to go down a path if that path (same remain target) has already been explored in another path

----BIG-O----
O(V+E) -- O(remain+nextRemain)?

'''


class Solution:
    from collections import deque

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount <= 0:
            return 0
        coins = set(coins)
        count = 1
        q = deque()
        q.append((amount, count))
        visited = set()
        visited.add(amount)

        while q:
            remain, count = q.popleft()
            if remain in coins:
                return count
            for c in coins:
                if remain - c > 0 and (remain - c) not in visited:
                    q.append((remain - c, count + 1))
                    visited.add(remain - c)
        return -1
