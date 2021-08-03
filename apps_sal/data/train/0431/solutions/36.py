class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        if N == 0:
            return 0
        mod = 10**9 + 7

        stack, left, right = [], [0] * N, [0] * N

        for i in range(N):
            count = 1
            while stack and stack[-1][0] > A[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((A[i], count))

        stack.clear()

        for i in range(N - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= A[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((A[i], count))

        return sum([l * r * v for l, r, v in zip(left, right, A)]) % mod
