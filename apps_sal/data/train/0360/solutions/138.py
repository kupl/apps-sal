class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(W: int) -> bool:
            count, total = 1, 0
            for w in weights:
                total += w
                if total > W:
                    count += 1
                    total = w
                    if count > D:
                        return False

            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
