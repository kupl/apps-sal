class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        [8, 7, 4, 2, 2, 1]
        n = len(piles)
        if n <= 1:
            return 0
        
        sorted_piles = sorted(piles, reverse=True)
        print(sorted_piles)
        s, e = 1, n-1
        ans = 0
        while s < e:
            ans += sorted_piles[s]
            s += 2
            e -= 1
        
        return ans
