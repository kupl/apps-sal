class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        @lru_cache(None)
        def max_sum_start_at(i):
            if i == len(arr) - 1:
                return arr[-1]
            return max(arr[i], arr[i] + max_sum_start_at(i + 1))

        @lru_cache(None)
        def max_sum_end_at(j):
            if j == 0:
                return arr[0]
            return max(arr[j], arr[j] + max_sum_end_at(j - 1))
        return max(max([max_sum_start_at(i) for i in range(len(arr))]), max([max_sum_end_at(i - 1) + max_sum_start_at(i + 1) for i in range(1, len(arr) - 1)]))
