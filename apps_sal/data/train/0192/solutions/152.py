class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, key=lambda x: -x)
        (ans, cnt) = (0, 0)
        for i in range(1, len(piles), 2):
            ans += piles[i]
            cnt += 1
            if cnt == len(piles) // 3:
                break
        return ans
