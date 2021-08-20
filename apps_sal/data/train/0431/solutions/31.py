class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = [-1]
        A.append(float('-inf'))
        res = 0
        for (i, num) in enumerate(A):
            while A[stack[-1]] > num:
                center = stack.pop()
                res += (i - center) * (center - stack[-1]) * A[center]
            stack.append(i)
        return res % (10 ** 9 + 7)
