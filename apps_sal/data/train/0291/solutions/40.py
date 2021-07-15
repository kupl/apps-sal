class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        odds = 0
        even = 0
        for i, c in enumerate(arr):
            if c & 1:
                odds, even = even + 1, odds
            else:
                even += 1
            res = (res + odds) % 1000000007
        return res % 1000000007

