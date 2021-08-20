class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        dp = []
        dp_forward = [0] * len(A)
        dp_backward = [0] * len(A)
        for i in range(len(A)):
            while dp and A[i] < dp[-1][0]:
                dp_forward[i] += dp.pop()[1] + 1
            dp.append([A[i], dp_forward[i]])
        print(dp_forward)
        dp = []
        for i in range(len(A) - 1, -1, -1):
            while dp and A[i] <= dp[-1][0]:
                dp_backward[i] += dp.pop()[1] + 1
            dp.append([A[i], dp_backward[i]])
        print(dp_backward)
        result = 0
        for i in range(len(A)):
            result += A[i] * (dp_forward[i] + 1) * (dp_backward[i] + 1)
        return result % (10 ** 9 + 7)
