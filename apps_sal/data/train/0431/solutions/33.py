class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        left = []
        right = []
        stack = []
        for i in range(len(A)):
            left.append(i + 1)
            right.append(len(A) - i)
        for i in range(len(A)):
            while stack and A[i] < A[stack[-1]]:
                poppedIdx = stack.pop()
                right[poppedIdx] = i - poppedIdx
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1
            stack.append(i)
        ans = 0
        for i in range(len(A)):
            ans = (ans + left[i] * right[i] * A[i]) % 1000000007
        return ans
