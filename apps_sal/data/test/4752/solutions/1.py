class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                return [d[target - num], i]
            d[num] = i

        new = sorted(nums)
        i, j = 0, -1
        for num in new:
            a, b = new[i], new[j]
            if a + b > target:
                j = j - 1
            elif a + b < target:
                i = i + 1
            elif a + b == target:
                if a != b:
                    ans = [nums.index(a), nums.index(b)]
                else:
                    m = nums.index(a)
                    nums.remove(a)
                    n = nums.index(b)
                    ans = [m, n + 1]
                return (ans)
