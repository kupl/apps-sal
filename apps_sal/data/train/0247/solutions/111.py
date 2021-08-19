class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sum = [float('inf')] * len(arr)
        suffix_sum = [float('inf')] * len(arr)
        prefix_map = {0: -1}
        suffix_map = {0: len(arr)}
        cur_sum = 0
        _min_till_now = float('inf')
        for i in range(len(arr) - 1):
            cur_sum += arr[i]
            if cur_sum - target in prefix_map:
                _min_till_now = min(_min_till_now, i - prefix_map[cur_sum - target])
            prefix_sum[i + 1] = _min_till_now
            prefix_map[cur_sum] = i
        cur_sum = 0
        _min_till_now = float('inf')
        for i in range(len(arr) - 1, -1, -1):
            cur_sum += arr[i]
            if cur_sum - target in suffix_map:
                _min_till_now = min(_min_till_now, suffix_map[cur_sum - target] - i)
            suffix_sum[i] = _min_till_now
            suffix_map[cur_sum] = i
        ans = min([x + y for (x, y) in zip(prefix_sum, suffix_sum)])
        return ans if ans != float('inf') else -1
