class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return 0
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.checkValidPartition(weights, mid, D):
                right = mid
            else:
                left = mid + 1
        return left

    def checkValidPartition(self, weights, capacity, D):
        count = 1
        cur_sum = 0
        for w in weights:
            if cur_sum + w > capacity:
                count += 1
                cur_sum = 0
            cur_sum += w
        return count <= D
