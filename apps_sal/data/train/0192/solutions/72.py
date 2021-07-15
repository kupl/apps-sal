class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        ans = 0
        i = len(piles) - 2
        c = 0
        while c != len(piles)//3:
            ans += piles[i]
            i-=2
            c+=1
        return ans
    # 1 2 2 4 7 8

