class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        def Kadane(arr, res = 0, cur = 0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        sm = sum(arr)
        if sm >= 0:
            sm = sm * k
        print (sum(arr), Kadane(arr))
        if k == 1:
            return max(sm, Kadane(arr)) % mod
        return max(sm, max(sum(arr), 0) * (k - 2) + Kadane(arr * 2)) % mod
