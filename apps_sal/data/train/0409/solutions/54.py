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

        def Kadane(arr, res=0, cur=0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod
