from functools import lru_cache


class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        vals = stoneValue
        n = len(vals)

        @lru_cache(None)
        def play(i):
            if i == n:
                return (0, 0)
            (p1, p2) = (-1000000000.0, -1)
            s = 0
            for j in range(i, min(i + 3, n)):
                s += vals[j]
                (p1_, p2_) = play(j + 1)
                p2_ += s
                if p2_ > p1:
                    p1 = p2_
                    p2 = p1_
            return (p1, p2)
        (p1, p2) = play(0)
        if p1 > p2:
            return 'Alice'
        elif p1 == p2:
            return 'Tie'
        return 'Bob'
