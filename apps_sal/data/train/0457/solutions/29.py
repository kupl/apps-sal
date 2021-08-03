from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        This a DP problem
        but we can solve this using BFS
        https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution
        '''

        if not amount:
            return 0

        queue = deque([(amount, 0)])
        visited = set([amount])
        while queue:
            remaining, steps = queue.popleft()

            for coin in coins:
                if coin == remaining:
                    return steps + 1
                elif coin < remaining:
                    temp = remaining - coin
                    if temp > 0 and temp not in visited:
                        visited.add(temp)
                        queue.append((temp, steps + 1))
        return -1
