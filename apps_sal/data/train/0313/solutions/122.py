class Solution:

    def producedAfterqDays(self, garden, adj, q):
        wat = [i - q for i in garden]
        return sum([len(list(cgen)) // adj for (c, cgen) in itertools.groupby(wat, key=lambda w: w <= 0) if c])

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 0
        r = max(bloomDay)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if self.producedAfterqDays(bloomDay, k, mid) >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
