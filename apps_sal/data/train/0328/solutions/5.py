class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        a= 1, b=3, c= 2
        """
        stack = []
        max_c = -math.inf
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max_c:
                return True
            while stack and stack[-1] < nums[i]:
                max_c = max(max_c, stack.pop())
            stack.append(nums[i])

        return False
