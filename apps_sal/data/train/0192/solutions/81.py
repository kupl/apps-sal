class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort Piles, iterate loops over 3 and add middle num
        # [1, 2, 2, 4, 7, 8] 7 + 2 = 9
        # [1, 2, 3, 4, 5, 6, 7, 8, 9] 2 + 5 + 8
        # [9, 8, 1] [7, 6, 2] [5, 4, 3] 8 + 6 + 4
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
