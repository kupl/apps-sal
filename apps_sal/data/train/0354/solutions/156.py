class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {(i, 1): 1 for i in range(6)}
        for i in range(n - 1):
            next_dp = collections.Counter()
            for (d, c), v in list(dp.items()):
                for cur in range(6):
                    if cur != d:
                        next_dp[(cur, 1)] += v
                    else:
                        if c + 1 <= rollMax[cur]:
                            next_dp[(cur, c + 1)] += v
            dp = next_dp

        return sum(dp.values()) % (10 ** 9 + 7)
