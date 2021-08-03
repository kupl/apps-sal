class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even = 0
        odd = 0
        for v in arr:
            if v % 2 == 0:
                even += 1
            else:
                even, odd = odd, even
                odd += 1
            ans += odd
        return ans % 1000000007
