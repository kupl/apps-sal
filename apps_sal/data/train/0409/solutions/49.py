class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        cum_sum = 0
        max_sum = 0
        MOD = 1000000007
        no_neg_num = True
        for var in arr:
            if var < 0:
                no_neg_num = False
        if no_neg_num:
            return sum(arr) * k
        for i in range(len(arr)):
            i = i % len(arr)
            cum_sum = max(cum_sum + arr[i], arr[i])
            if cum_sum > 0:
                cum_sum %= MOD
            max_sum = max(cum_sum, max_sum)
        if k == 1:
            return max_sum
        cum_sum2 = 0
        max_sum2 = 0
        for i in range(len(arr) * 2):
            i = i % len(arr)
            cum_sum2 = max(cum_sum2 + arr[i], arr[i])
            if cum_sum2 > 0:
                cum_sum2 %= MOD
            max_sum2 = max(cum_sum2, max_sum2)
        if sum(arr) > 0:
            return (max_sum + sum(arr) % MOD * (k - 1)) % MOD
        else:
            return max_sum2
