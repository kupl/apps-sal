from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix_sums = [0]
        current_sum = 0
        for right in range(len(A)):
            current_sum += A[right]
            prefix_sums.append(current_sum)
        # print(prefix_sums)
        best = 0
        left = 0
        memo = dict()
        while left + L <= len(A) and left + L < len(prefix_sums):
            limits = ((0, left), (left + L, len(prefix_sums)))
            best_m = self.get_max_subarray(prefix_sums, M, limits, memo)
            subarray_sum = best_m[0] + prefix_sums[left + L] - prefix_sums[left]
            # if subarray_sum > best:
            #     print(f'{A[best_m[1]:best_m[2]]}={best_m[0]}')
            #     print(f'{A[left:left+L]}={subarray_sum-best_m[0]}')
            best = max(best, subarray_sum)
            left += 1
        return best

    def get_max_subarray(self, sums, length, limits, memo):
        # stores highest sum as tuple of (sum, left, right (exclusive))
        if (length, limits) in memo:
            return memo[(length, limits)]
        high_score = (0, 0, 0)
        for limit in limits:
            left = limit[0]
            # test subarrays of length within limit[0] and limit[1] (excluding limit[1])
            while left + length <= limit[1] and left + length < len(sums):
                subarray_sum = sums[left + length] - sums[left]
                # print(f'{left}:{left+length}={subarray_sum}')
                high_score = max(high_score, (subarray_sum, left, left + length))
                # print(f'high: {high_score}')
                left += 1
        memo[(length, limits)] = high_score
        return high_score
