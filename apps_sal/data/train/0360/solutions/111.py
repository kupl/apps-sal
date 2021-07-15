class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canFitInD(m):
            n = 1
            current = 0
            for i in range(len(weights)):
                if current + weights[i] <= m:
                    current += weights[i]
                else:
                    n += 1
                    current = weights[i]
                    if n > D:
                        return False
            return True

        while l < r:
            mid = l + (r - l)//2
            if canFitInD(mid):
                r = mid
            else:
                l = mid+1

        return l
# leetcode submit region end(Prohibit modification and deletion)

