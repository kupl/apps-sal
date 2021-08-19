class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total = sum(weights)
        lb = max(weights)
        ub = total
        while lb < ub:
            mid = lb + (ub - lb) // 2
            if self.checkIfCanShipWithinDDays(weights, D, mid):
                ub = mid
            else:
                lb = mid + 1
        return lb

    def checkIfCanShipWithinDDays(self, weights: List[int], D: int, capacity: int) -> bool:
        (b, count, total) = (0, 0, 0)
        while b < len(weights):
            while total + weights[b] <= capacity:
                total += weights[b]
                b += 1
                if b == len(weights):
                    count += 1
                    return count <= D
            count += 1
            total = 0
        return count <= D
