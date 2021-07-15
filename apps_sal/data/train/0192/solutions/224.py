class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        you = []
        l = int((len(piles)/3))
        piles.sort()
        piles = piles[l:]
        for i in range(len(piles)):
            if i%2 == 0:
                you.append(piles[i])
        return sum(you)
