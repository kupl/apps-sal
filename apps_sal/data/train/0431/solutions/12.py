class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        tot = 0
        stack = [-1]
        A.append(0)
        for i in range(len(A)):
            while A[i] < A[stack[-1]]:
                loc = stack.pop()
                height = A[loc]
                left = loc - stack[-1]
                right = i - loc
                width = i - stack[-1] - 1
                tot += height * left * right
            stack.append(i)
        return tot % (10 ** 9 + 7)
