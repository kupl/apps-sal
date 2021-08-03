class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        cache = {}

        def helper(n):
            if n in cache:
                return cache[n]
            s = sqrt(n)
            if s.is_integer():
                cache[n] = True
                return True
            i = 1
            while i < s:
                j = i * i
                if not helper(n - j):
                    cache[n] = True
                    return True
                i += 1
            cache[n] = False
            return False
        return helper(n)
