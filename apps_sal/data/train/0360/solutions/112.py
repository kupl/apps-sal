class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        if not n:
            return n
        total = sum(weights)
        target = total // D
        (left, right) = (max(weights), total)

        def check(s, total, D):
            cur = 0
            i = 0
            while i < len(weights):
                w = weights[i]
                if cur + w > s:
                    total -= cur
                    D -= 1
                    cur = 0
                else:
                    cur += w
                    i += 1
                if D == 1:
                    if total > s:
                        return False
                    else:
                        return True
            return True
        ans = total
        while left <= right:
            mid = (left + right + 1) // 2
            if check(mid, total, D):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
