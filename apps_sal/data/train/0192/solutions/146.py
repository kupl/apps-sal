class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        newP = []
        pileSort = sorted(piles)

        while(len(pileSort) > 0):
            newP.append([pileSort[0], pileSort[-2], pileSort[-1]])
            pileSort.pop(0)
            pileSort.pop(-2)
            pileSort.pop(-1)

        sum = 0

        for i in newP:
            sum += i[1]

        return sum
