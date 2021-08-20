class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]

        def kadane(it):
            max_ = current = float('-inf')
            for num in it:
                current = num + max(current, 0)
                max_ = max(max_, current)
            return max_
        total = sum(A)
        max1 = kadane((num for num in A))
        max2 = total + kadane((-A[idx] for idx in range(n - 1)))
        max3 = total + kadane((-A[idx] for idx in range(1, n)))
        return max(max1, max2, max3)
