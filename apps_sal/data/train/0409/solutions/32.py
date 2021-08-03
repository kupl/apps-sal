class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        mod = 10**9 + 7

        def Kadane(arr):
            sum_till_now = 0
            max_sum = 0
            for i in range(len(arr)):
                sum_till_now += arr[i]
                sum_till_now = max(sum_till_now, arr[i])
                max_sum = max(max_sum, sum_till_now)
            return max_sum
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod
