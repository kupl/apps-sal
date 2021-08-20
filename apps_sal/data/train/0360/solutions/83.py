class Solution:

    def canFinish(self, weights, D, C):
        index = 0
        for _ in range(D):
            total = 0
            while index < len(weights) and total + weights[index] <= C:
                total += weights[index]
                index += 1
            if index == len(weights):
                return True
        return False

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = 0
        r = sum(weights)
        while l < r - 1:
            m = l + (r - l) // 2
            if self.canFinish(weights, D, m):
                r = m
            else:
                l = m + 1
        if self.canFinish(weights, D, l):
            return l
        return r
