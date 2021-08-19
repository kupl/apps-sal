from collections import defaultdict


class Solution:

    def canShipWithinDays(self, weights: List[int], D: int, maxWeight: int) -> bool:
        if max(weights) > maxWeight:
            return False
        shipmentweights = [0]
        for w in weights:
            if shipmentweights[-1] + w <= maxWeight:
                shipmentweights[-1] += w
            else:
                shipmentweights.append(w)
        return len(shipmentweights) <= D

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        maxweight = sum(weights)
        minweight = max(weights)
        while maxweight > minweight + 1:
            mw = (maxweight + minweight) // 2
            if self.canShipWithinDays(weights, D, mw):
                maxweight = mw
            else:
                minweight = mw
        if self.canShipWithinDays(weights, D, minweight):
            return minweight
        else:
            return maxweight
