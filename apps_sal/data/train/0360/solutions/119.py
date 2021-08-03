def isOK(cap, weights, D):
    cnt = 1
    total = 0
    for i in range(len(weights)):
        if total + weights[i] > cap:
            cnt += 1
            total = weights[i]
        else:
            total += weights[i]
    return cnt <= D


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), max(weights) * len(weights) // D

        while left <= right:
            mid = (right + left) // 2
            if isOK(mid, weights, D):
                right = mid - 1
            else:
                left = mid + 1
        return left
