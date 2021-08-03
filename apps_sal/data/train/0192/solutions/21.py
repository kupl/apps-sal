class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        i = 1
        x = len(piles)
        ans = []
        while i < x:

            ans.append(piles[i])
            x = x - 1

            i = i + 2

        return sum(ans)
