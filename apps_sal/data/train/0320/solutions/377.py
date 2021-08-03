def adjust2power(n):
    if n == 0:
        return 0
    for i in range(1, n + 1):
        if 1 << i >= n:
            if n % (1 << i) != 0:
                i -= 1
            break
    return 1 << i


def howManyPower(n):
    for i in range(1, n + 1):
        if 1 << i == n:
            return i


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums2p = []  # nums of 2 powers
        ans = 0
        while max(nums) > 1:
            ans += 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                if nums[i] > 1:
                    ans += nums[i] % 2
                nums[i] = max(nums[i] // 2, 1)
 #           print(nums)
        return ans + len(nums) - nums.count(0)
