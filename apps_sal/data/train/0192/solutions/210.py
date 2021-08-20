class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count1 = int(len(piles) / 3)
        sum1 = 0
        j = 0
        while count1 < len(piles):
            print(j, count1)
            if j % 2 == 0:
                print(piles[count1])
                sum1 = sum1 + piles[count1]
            count1 = count1 + 1
            j = j + 1
        return sum1
