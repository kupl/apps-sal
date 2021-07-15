class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        
        def kadane(arr):
            for i in range(1, len(arr)):
                arr[i] += arr[i - 1] if arr[i - 1] > 0 else 0
            return max(max(arr), 0)
        
        if k <= 2:
            return kadane(arr * k) % mod
        return (kadane(arr * 2) + (k - 2) * max(sum(arr), 0)) % mod        
        
        # s = sum(arr)
        # if s < 
        # mod = 10 ** 9 + 7
        # nums = arr * 2
        # n = len(arr)
        # for i in range(1, len(nums)):
        #     if nums[i - 1] > 0:
        #         nums[i] += nums[i - 1]
        # if k <= 2:
        #     max_sum = max(nums[: n * k])
        #     return max_sum % mod if max_sum >= 0 else 0
        # n1, n2 = max(nums[n: 2 * n]), max(nums[2 * n: 3 * n])
        # if n2 > n1:
        #     return n1 + (k - 2) * (n2 - n1) % mod
        # else:
        #     return n1 % mod if n1 >= 0 else 0
        
        
        def Kadane(arr, res = 0, cur = 0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod
