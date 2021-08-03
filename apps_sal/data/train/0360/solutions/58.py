class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        minCapacity, maxCapacity = max(weights), sum(weights)

        while minCapacity < maxCapacity:
            capacityCandidate = (minCapacity + maxCapacity) // 2
            daysToShip, currentCargo = 1, 0

            for newCargo in weights:
                if currentCargo + newCargo > capacityCandidate:
                    currentCargo = 0
                    daysToShip += 1
                currentCargo += newCargo

            if daysToShip <= D:
                maxCapacity = capacityCandidate
            else:
                minCapacity = capacityCandidate + 1

        return minCapacity
