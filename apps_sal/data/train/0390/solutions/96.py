import math
from collections import defaultdict


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        def dfs(position, player):
            if position in cache:
                if cache[position] == True:
                    return player
                return not player
            for sq in squares:
                if sq == position:
                    cache[position] = player
                    return player
                if sq > position:
                    break
                if player == dfs(position - sq, not player):
                    cache[position] = player
                    return player
            cache[position] = not player
            return not player
        cache = defaultdict(bool)
        max_val = int(math.sqrt(n))
        squares = [1]
        for i in range(2, max_val + 1):
            squares.append(i ** 2)
        cache[1] = True
        cache[2] = False
        cache[3] = True
        cache[4] = True
        for i in range(5, n + 1):
            cache[i] = dfs(i, True)
        return cache[n]
