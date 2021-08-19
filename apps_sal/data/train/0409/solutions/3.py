class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MAX_INT = 10 ** 9 + 7

        def kadane(arr):
            (cur, res) = (0, 0)
            for v in arr:
                cur = max(v, cur + v)
                res = max(res, cur)
            return res
        if k == 1:
            return kadane(arr)
        else:
            s = sum(arr)
            if s <= 0:
                return kadane(arr * 2)
            else:
                return (kadane(arr) + (k - 1) * s) % MAX_INT
