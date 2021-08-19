from collections import deque


def addMinStack(stack, val):
    while stack and stack[-1] > val:
        stack.pop()
    stack.append(val)


def addMaxStack(stack, val):
    while stack and stack[-1] < val:
        stack.pop()
    stack.append(val)


def delStack(stack, val):
    if stack and stack[0] == val:
        stack.popleft()


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        minstack = deque([])
        maxstack = deque([])
        start = 0
        end = 0
        maxSubArray = 0
        while end < len(nums):
            addMinStack(minstack, nums[end])
            addMaxStack(maxstack, nums[end])
            if maxstack[0] - minstack[0] > limit:
                while maxstack[0] - minstack[0] > limit:
                    delStack(minstack, nums[start])
                    delStack(maxstack, nums[start])
                    start += 1
            maxSubArray = max(maxSubArray, end - start + 1)
            end += 1
        return maxSubArray
