class Solution:

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None or len(nums) == 0:
            return ''
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, len(nums) - i - 1, -1):
                e1 = str(nums[j - 1])
                e2 = str(nums[j])
                if e1 + e2 < e2 + e1:
                    t = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = t
        ans = ''
        for n in nums:
            if n == 0 and ans == '':
                continue
            ans += str(n)
        return '0' if len(ans) == 0 else ans
