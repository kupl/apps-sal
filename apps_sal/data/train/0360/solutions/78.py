class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = 1
        right = max(weights) * len(weights)
        while left < right:
            mid = (left + right) // 2
            if self.possible(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def possible(self, weights, D, mid):
        cnt = 0
        tmp = 0
        for w in weights:
            if w > mid:
                return False
            if tmp + w > mid:
                tmp = w
                cnt += 1
            else:
                tmp += w
        if tmp != 0:
            cnt += 1
        return cnt <= D
