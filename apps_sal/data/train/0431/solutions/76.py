import numpy as np


class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        (left, right) = ([], [])
        for i in range(len(A)):
            cnt = 1
            while stack and A[i] <= stack[-1][0]:
                cnt += stack[-1][1]
                stack.pop()
            stack.append([A[i], cnt])
            left.append(cnt)
        stack = []
        for i in range(len(A) - 1, -1, -1):
            cnt = 1
            while stack and A[i] < stack[-1][0]:
                cnt += stack[-1][1]
                stack.pop()
            stack.append([A[i], cnt])
            right.append(cnt)
        right = right[::-1]
        res = 0
        for i in range(len(A)):
            res += A[i] * left[i] * right[i]
        return res % (10 ** 9 + 7)
