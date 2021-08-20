class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total = sum(weights)
        maxW = max(weights)
        low = total // D
        high = low + maxW

        def isok(weights, D, cap):
            curr = cap
            count = 1
            for w in weights:
                if w > cap:
                    return False
                if curr - w < 0:
                    count += 1
                    curr = cap - w
                else:
                    curr -= w
            return count <= D
        while low != high:
            mid = (low + high) // 2
            if isok(weights, D, mid):
                high = mid
            else:
                low = mid + 1
        return low
