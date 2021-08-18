from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix_sums = [0]
        current_sum = 0
        for right in range(len(A)):
            current_sum += A[right]
            prefix_sums.append(current_sum)
        best = 0
        left = 0
        memo = dict()
        while left + L <= len(A) and left + L < len(prefix_sums):
            limits = ((0, left), (left + L, len(prefix_sums)))
            best_m = self.get_max_subarray(prefix_sums, M, limits, memo)
            subarray_sum = best_m[0] + prefix_sums[left + L] - prefix_sums[left]
            best = max(best, subarray_sum)
            left += 1
        return best

    def get_max_subarray(self, sums, length, limits, memo):
        if (length, limits) in memo:
            return memo[(length, limits)]
        high_score = (0, 0, 0)
        for limit in limits:
            left = limit[0]
            while left + length <= limit[1] and left + length < len(sums):
                subarray_sum = sums[left + length] - sums[left]
                high_score = max(high_score, (subarray_sum, left, left + length))
                left += 1
        memo[(length, limits)] = high_score
        return high_score
