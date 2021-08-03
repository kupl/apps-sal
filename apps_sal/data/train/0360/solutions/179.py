class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def can_ship(x):
            cnt = 1
            curr = 0
            for w in weights:
                if w > x:
                    return False

                if curr + w > x:
                    curr = w
                    cnt += 1
                else:
                    curr += w

                if cnt > D:
                    return False

            return cnt <= D

        left, right = 1, sum(weights)
        while left < right:
            mid = (right - left) // 2 + left

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left
