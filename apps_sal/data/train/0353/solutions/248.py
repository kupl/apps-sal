import math


class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        check = {0: 1}
        nums.sort()
        n = len(nums)
        right = n - 1
        cur = 1
        for i in range(1, n + 1):
            cur = 2 * cur % 1000000007
            check[i] = cur
        result = 0
        for i in range(n):
            while right >= i and nums[i] + nums[right] > target:
                right -= 1
            if right < i:
                break
            extra = right - i
            if nums[i] + nums[right] <= target:
                result += check[extra] % 1000000007
        return result % 1000000007
