class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        nums = []
        for hour in hours:
            if hour > 8:
                nums.append(1)
            else:
                nums.append(-1)
        prevsum, sumv = [], 0
        for num in nums:
            sumv += num
            prevsum.append(sumv)
        stack = []
        prevsum = [0] + prevsum
        for i, val in enumerate(prevsum):
            if not stack or prevsum[stack[-1]] > val:
                stack.append(i)
        i, res = len(prevsum) - 1, 0
        while i >= 0:
            while stack and prevsum[stack[-1]] < prevsum[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1
        return res

