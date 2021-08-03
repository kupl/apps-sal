class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        m = 10**9 + 7

        def kadane(arr):
            cur = 0
            res = 0
            for a in arr:
                cur = max(a, cur + a)
                res = max(res, cur)

            return res
        if k == 1:
            return kadane(arr)
        else:
            if sum(arr) <= 0:
                return kadane(arr * 2)
            else:
                return (kadane(arr) + (k - 1) * sum(arr)) % m
