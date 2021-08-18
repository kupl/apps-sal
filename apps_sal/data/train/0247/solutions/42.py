

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        prefix_sum = {0: -1}
        cur_sum = 0
        for i, val in enumerate(arr):
            cur_sum += val
            prefix_sum[cur_sum] = i

        left_min_len = float('inf')
        ans = float('inf')
        cur_sum = 0
        for i, val in enumerate(arr):
            cur_sum += val
            if (cur_sum - target) in prefix_sum:
                left_min_len = min(left_min_len, i - prefix_sum[cur_sum - target])
            if (cur_sum + target) in prefix_sum:
                ans = min(ans, left_min_len + prefix_sum[cur_sum + target] - i)

        return ans if ans < float('inf') else -1
