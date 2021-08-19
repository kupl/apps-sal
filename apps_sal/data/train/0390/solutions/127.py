class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        winmap = {}
        winmap[0] = False
        winmap[1] = True

        def fill_map(n):
            if n in winmap:
                return winmap[n]
            i = 1
            winmap[n] = 0
            while i * i <= n:
                winmap[n] = winmap[n] or not fill_map(n - i * i)
                if winmap[n]:
                    break
                i += 1
            return winmap[n]
        for i in range(1, n):
            fill_map(n)
        return winmap[n]
