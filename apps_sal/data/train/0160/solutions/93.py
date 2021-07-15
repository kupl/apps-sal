class Solution:
    
    @staticmethod
    def f(piles, start, end, cache, sums):
        if cache[start][end] == -1:
            cache[start][end] = max(
                piles[start] + sums[end + 1] - sums[start + 1] - Solution.f(piles, start + 1, end, cache, sums),
                piles[end] + sums[end] - sums[start] - Solution.f(piles, start, end - 1, cache, sums)
            )
        return cache[start][end]
    
    def stoneGame(self, piles: List[int]) -> bool:
        cache = [[-1] * len(piles) for i in range(len(piles))]
        sums = [0] * (len(piles) + 1)
        for i in range(len(piles)):
            sums[i + 1] = sums[i] + piles[i]
            cache[i][i] = piles[i]
        alex = Solution.f(piles, 0, len(piles) - 1, cache, sums)
        return alex > sums[-1] - alex

