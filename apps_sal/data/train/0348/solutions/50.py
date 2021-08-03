class Solution:
    def maximumSum(self, a: List[int]) -> int:
        n = len(a)
        ans = skipped = not_skipped = a[-1]
        for i in range(n - 2, -1, -1):
            not_skipped, skipped = max(a[i], a[i] + not_skipped, skipped), max(a[i], a[i] + skipped)
            ans = max(ans, skipped, not_skipped)
        return ans
