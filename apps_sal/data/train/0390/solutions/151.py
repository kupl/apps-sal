class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        table = [False for x in range(n+1)]
        for x in range(1, n+1):
            flag = False
            c = 1
            while c**2 <= x:
                if not table[x-c**2]:
                    flag = True
                    break
                c += 1
            table[x] = flag
        return table[-1]
