class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = ans = 0
        mod = 10 ** 9 + 7
        for num in arr:
            if num % 2 == 1:
                ans += even + 1
                curr_even = even
                even = odd
                odd = curr_even + 1
            else:
                ans += odd
                even += 1
        return ans % mod
