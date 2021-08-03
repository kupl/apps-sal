class Solution:
    def maxCoins(self, a: List[int]) -> int:
        a.sort()
        n = len(a)
        i = n // 3
        ans = 0
        while i < n:
            ans += a[i]
            i += 2
        return ans
