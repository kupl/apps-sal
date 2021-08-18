class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = odd = even = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                even = even + 1
                ans += odd
            else:
                even, odd = odd, even + 1
                ans += odd

        return ans % (10**9 + 7)
