class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        (left, right) = ([], [])
        stack = []
        for i in range(len(A)):
            count = 1
            while stack and stack[-1][0] > A[i]:
                count += stack.pop()[1]
            stack.append([A[i], count])
            left.append(count)
        stack = []
        for i in reversed(range(len(A))):
            count = 1
            while stack and stack[-1][0] >= A[i]:
                count += stack.pop()[1]
            stack.append([A[i], count])
            right.append(count)
        right = right[::-1]
        res = 0
        for i in range(len(A)):
            res += left[i] * right[i] * A[i]
        return res % (10 ** 9 + 7)
