class Solution:
    def minDays(self, bd: List[int], m: int, k: int) -> int:
        if m * k > len(bd):
            return -1

        def helper(d):
            ans, cur = 0, 0
            for b in bd:
                cur = 0 if b > d else cur + 1
                if cur == k:
                    ans += 1
                    cur = 0
            return ans

        days = sorted(set(bd))
        l, h = 0, len(days) - 1
        while l < h:
            mid = (l + h) // 2
            if helper(days[mid]) < m:
                l = mid + 1
            else:
                h = mid

        return days[h] if helper(days[h]) >= m else -1
