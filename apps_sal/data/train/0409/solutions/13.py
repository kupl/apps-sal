MOD = 1000000007
class Solution:
    def kConcatenationMaxSum(self, arr, k):
        min_pre_sum = 0
        pre_sum = 0
        max_pre_sum, max_suf_sum, max_win_sum = 0, 0, 0
        n = len(arr)
        for i in range(n):
            pre_sum += arr[i]
            max_win_sum = max(max_win_sum, pre_sum - min_pre_sum)
            if i == n - 1:
                max_suf_sum = pre_sum - min_pre_sum
            min_pre_sum = min(min_pre_sum, pre_sum)
            max_pre_sum = max(max_pre_sum, pre_sum)
        if k == 1:
            return max_win_sum
        if pre_sum > 0:
            return max(max_win_sum, max_pre_sum + max_suf_sum + (k - 2) * pre_sum) % MOD
        else:
            return max(max_win_sum, max_pre_sum + max_suf_sum) % MOD
