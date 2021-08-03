import numpy as np


class Solution:
    #     def __init__(self):
    #         self.subar = []
    #         self.mins = []
    #         self.mins_sum = 0

    #     def getSubarrays(self, A):
    #         min_cur = A[0]
    #         for i in range(len(A)):
    #             if A[i] < min_cur:
    #                 min_cur = A[i]
    #                 # print(min_cur)
    #             self.mins_sum += min_cur
    #             # print(A[:(i+1)], \"min {} sum {}\".format(min_cur, self.mins_sum))
    #             # self.mins.append(min_cur)
    #             # self.subar.append(A[:i])

    #         if len(A) > 1:
    #             self.getSubarrays(A[1:])

    #     def sumSubarrayMins(self, A: List[int]) -> int:
    #         if len(A) > 0: self.getSubarrays(A)
    #         # print(self.subar)
    #         # mins = [np.min(arr) for arr in self.subar]
    #         # print(mins)
    #         # return int(np.sum(mins) % (10**9 + 7))
    #         return int(self.mins_sum % (10**9 + 7))

    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        left, right = [], []
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
        # print(left, right)
        res = 0
        for i in range(len(A)):
            res += A[i] * left[i] * right[i]

        return res % (10**9 + 7)
