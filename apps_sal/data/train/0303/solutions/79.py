class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp_sum = [0] * n
        dp_sum[0] = arr[0]
        max_so_far = arr[0]
        for i in range(1, k):
            max_so_far = max(max_so_far, arr[i])
            dp_sum[i] = (i + 1) * max_so_far
        for i in range(k, n):
            partition_max = 0
            for back in range(k):
                partition_max = max(partition_max, arr[i - back])
                dp_sum[i] = max(dp_sum[i], dp_sum[i - back - 1] + (back + 1) * partition_max)
        return dp_sum[-1]
