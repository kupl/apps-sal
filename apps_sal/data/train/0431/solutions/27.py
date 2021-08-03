class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        length = len(A)
        left = [-1 for _ in range(length)]
        right = [length for _ in range(length)]
        stack, res, N = [], 0, 10 ** 9 + 7

        for i in range(length):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # print(left)
        # print(right)

        for i in range(length):
            res += (i - left[i]) * (right[i] - i) * A[i]
        return res % N
