class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def kadane(ls, n):
            max_sum_so_far = ls[0]
            current_sum = ls[0]
            for i in range(1, n):
                current_sum = max(current_sum + ls[i], ls[i])
                max_sum_so_far = max(max_sum_so_far, current_sum)
            return max_sum_so_far
        n = len(arr)
        first_max_sum = kadane(arr, n)
        if k <= 1:
            return first_max_sum
        arr_sum = sum(arr)
        arr.extend(arr)
        next_max_sum = kadane(arr, 2 * n)

        if arr_sum < 0:
            return max(next_max_sum, 0)

        if arr_sum >= 0 and next_max_sum > arr_sum:
            return (next_max_sum + (k - 2) * arr_sum) % (10**9 + 7)

        return max(first_max_sum, 0)
