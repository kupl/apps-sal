MOD = 1000000007


class Solution:
    def numOfSubarrays(self, arr):
        n = len(arr)
        pre_sum = [1, 0]
        now_sum = 0
        res = 0
        for i in range(n):
            now_sum ^= (arr[i] & 1)
            if now_sum == 1:
                res += pre_sum[0]
                pre_sum[1] += 1
            else:
                res += pre_sum[1]
                pre_sum[0] += 1
        return res % MOD
