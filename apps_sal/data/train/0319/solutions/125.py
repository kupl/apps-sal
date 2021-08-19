class Solution:

    def stoneGameIII(self, piles: List[int]) -> str:
        N = len(piles)

        @lru_cache(None)
        def sg(idx, turn):
            if idx == N:
                return 0
            res = float('-inf')
            if turn == -1:
                res = float('inf')
            ps = 0
            for i in range(idx, min(idx + 3, N)):
                ps += piles[i]
                nxt = ps * turn + sg(i + 1, -turn)
                if turn == 1:
                    res = max(res, nxt)
                else:
                    res = min(res, nxt)
            return res
        res = sg(0, 1)
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        return 'Tie'
