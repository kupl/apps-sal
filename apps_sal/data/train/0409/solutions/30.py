class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def Kadane(arr):
            ans, cur = 0, 0
            for num in arr:
                cur = max(cur + num, num)
                ans = max(ans, cur)
            return ans
        return (((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) if k > 1 else Kadane(arr)) % (10 ** 9 + 7)
