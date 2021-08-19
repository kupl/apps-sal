class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        (ans, odd, even) = (0, 0, 0)
        for i in arr:
            if i & 1:
                (odd, even) = (even + 1, odd)
            else:
                even = even + 1
            ans += odd
        return ans % (10 ** 9 + 7)
