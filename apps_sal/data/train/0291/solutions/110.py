class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        (odd_sum, even_sum, cur_sum, ans) = (0, 1, 0, 0)
        mod = 10 ** 9 + 7
        for i in arr:
            cur_sum += i
            if cur_sum % 2 != 0:
                odd_sum += 1
                ans += even_sum % mod
            if cur_sum % 2 == 0:
                even_sum += 1
                ans += odd_sum % mod
        ans = ans % mod
        return ans
