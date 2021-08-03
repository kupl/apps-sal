class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        res = 0
        prev = ''
        pool = []

        for c, v in zip(s + ' ', cost + [0]):
            if c != prev:
                if len(pool) > 1:
                    res += sum(pool) - max(pool)
                prev = c
                pool = [v]
            else:
                pool.append(v)

        return res
