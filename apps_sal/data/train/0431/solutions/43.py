class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        ple_stack = []
        left = [-1] * len(A)
        for i in range(len(A)):
            while ple_stack and A[i] < A[ple_stack[-1]]:
                ple_stack.pop()
            left[i] = ple_stack[-1] if ple_stack else -1
            ple_stack.append(i)
        for i in range(len(A)):
            left[i] = i - left[i]

        nle_stack = []
        right = [-1] * len(A)
        for j in reversed(range(len(A))):
            while nle_stack and A[j] <= A[nle_stack[-1]]:
                nle_stack.pop()
            right[j] = nle_stack[-1] if nle_stack else len(A)
            nle_stack.append(j)
        for j in range(len(A)):
            right[j] = right[j] - j

        return sum([x * y * z for x, y, z in zip(left, right, A)]) % (10**9 + 7)
