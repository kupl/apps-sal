class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7

        cumu, cumu_cumu = [0] * (n + 1), [0] * (n + 1)
        for i, v in enumerate(nums):
            cumu[i + 1] = v + cumu[i]
            cumu_cumu[i + 1] = cumu[i + 1] + cumu_cumu[i]

        def count_subarray_sum_less_equal_target(target):
            nonlocal cumu
            answer = left = 0
            for right, v in enumerate(cumu):
                while v - cumu[left] > target:
                    left += 1
                answer += right - left
            return answer

        def kth_sum(k):
            nonlocal cumu
            lo, hi = 0, cumu[-1]
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if count_subarray_sum_less_equal_target(mid) < k:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def sum_first_k_subarray_sum(k):
            nonlocal cumu, cumu_cumu, MOD

            target = kth_sum(k)

            answer = left = 0
            for right, v in enumerate(cumu):
                while v - cumu[left] > target:
                    left += 1
                answer += v * (right - left + 1) - cumu_cumu[right] + (cumu_cumu[left - 1] if left else 0)
                answer %= MOD
            return answer - (count_subarray_sum_less_equal_target(target) - k) * target

        return (MOD + sum_first_k_subarray_sum(right) - sum_first_k_subarray_sum(left - 1)) % MOD
