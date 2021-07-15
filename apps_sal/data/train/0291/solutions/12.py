class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even = 0
        odd = 0
        for v in arr:
            if v % 2 == 0:
                even, odd = (even + 1)  % 10000000007, odd
            else:
                even, odd = odd, (even + 1)  % 10000000007
            ans = (ans + odd) % 10000000007
        return ans  % 1000000007
