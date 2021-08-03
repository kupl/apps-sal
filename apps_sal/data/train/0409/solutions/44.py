class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        mod = 10**9 + 7

        def helper(arr, res=0, cur=0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            print(res)
            return res
        return ((k - 2) * max(sum(arr), 0) + helper(arr * 2)) % mod if k > 1 else helper(arr) % mod
