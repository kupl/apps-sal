class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return None
        max_sum = [0] * len(arr)
        max_sum_one_del = [0] * len(arr)
        max_sum[0] = arr[0]
        max_sum_one_del[0] = arr[0]
        for i in range(1, len(arr)):
            max_sum[i] = max(max_sum[i - 1] + arr[i], arr[i])
            max_sum_one_del[i] = max(max_sum_one_del[i - 1] + arr[i], arr[i])
            if i > 1:
                max_sum_one_del[i] = max(max_sum[i - 2] + arr[i], max_sum_one_del[i])
        return max(max_sum_one_del)
