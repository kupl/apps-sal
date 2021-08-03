class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''
        Every time when I choose the best I can do is to get the 2nd largest pile among all
        I also want to make sure Bob gets the smallest pile
        '''
        piles.sort(reverse=True)
        ans = 0
        for i in range(1, len(piles) // 3 + 1):
            ans += piles[2 * (i - 1) + 1]
        return ans
