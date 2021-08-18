from functools import lru_cache


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        '''
        build the neighbors dictionary
        
        neighbors to a key are the keys reachable to itself from a key
        '''
        neighbors = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0),
                     5: (), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4)}

        @lru_cache(maxsize=None)
        def num_ways(key, n):
            if n == 0:
                return 0
            if n == 1:
                return len(neighbors[key])

            w = 0
            for neighbor in neighbors[key]:
                w += num_ways(neighbor, n - 1)
            return w

        answer = 0
        for i in range(10):
            answer += num_ways(i, n - 1)

        answer %= (pow(10, 9) + 7)
        return answer
