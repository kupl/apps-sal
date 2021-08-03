class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        odd = 0
        even = 0
        ans = 0
        for num in arr:
            if num % 2:
                odd, even = even + 1, odd
            else:
                even += 1
            ans = (ans + odd) % mod
        return ans
