class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left_less = [0] * n
        right_less = [0] * n
        left_stack = []
        right_stack = []
        for i in range(n):
            count = 1
            while left_stack and left_stack[-1][0] > A[i]:
                count += left_stack.pop()[1]
                # count += 1
            left_less[i] = count
            left_stack.append([A[i], count])
        for i in range(n - 1, -1, -1):
            count = 1
            while right_stack and right_stack[-1][0] >= A[i]:
                count += right_stack.pop()[1]
                # count += 1
            right_less[i] = count
            right_stack.append([A[i], count])

        mod = 10**9 + 7
        return sum(A[i] * right_less[i] * left_less[i] for i in range(n)) % mod
