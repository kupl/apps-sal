class Solution:
    # Ref: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/discuss/755495/Python-or-O(n)-time-and-O(1)-space-or-prefix-sum(detailed-explanation)
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_sum, even_sum, cur_sum, ans = 0, 1, 0, 0
        mod = (10**9 + 7)
        for i in arr:
            cur_sum += i

            # Check for odd sum
            if cur_sum % 2 != 0:
                odd_sum += 1
                ans += even_sum % mod

            # Check for even sum
            if cur_sum % 2 == 0:
                even_sum += 1
                ans += odd_sum % mod

        ans = ans % mod

        return ans
