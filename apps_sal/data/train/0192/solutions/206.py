class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        me, alice, bob = len(piles)-2, 0, len(piles)
        ans = 0
        while alice < me:
            ans += piles[me]
            alice += 1
            me -= 2
            bob -= 2
        return ans
            
            

