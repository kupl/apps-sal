class Solution:

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        for num in nums:
            if not stack or num < stack[-1][0]:
                stack.append([num, num])
            elif num > stack[-1][0]:
                if num < stack[-1][1]:
                    return True
                else:
                    node = stack.pop()
                    while stack and num >= stack[-1][1]:
                        stack.pop()
                    if stack and num > stack[-1][0]:
                        return True
                    stack.append([node[0], num])
        return False
