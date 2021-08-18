class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        x = 0
        test = []
        piles.sort()
        for i in range(len(piles) - 2, 0, -2):
            if (x != len(piles) // 3):
                res += piles[i]
                test.append(piles[i])
                x += 1
        print(test)
        return res
