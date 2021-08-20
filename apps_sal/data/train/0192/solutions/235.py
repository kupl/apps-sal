class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        myNum = 0
        piles.sort(reverse=True)
        for i in range(1, len(piles) * 2 // 3 + 1, 2):
            myNum += piles[i]
            print(myNum)
        return myNum
