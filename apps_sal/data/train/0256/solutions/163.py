class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if H == len(piles):
            return max(piles)
        else:
            if sum(piles) % H == 0:
                tempMin = sum(piles) // H
            else:
                tempMin = sum(piles) // H + 1
            tempMax = max(piles)
            while tempMin != tempMax:
                tempMid = (tempMax - tempMin) // 2 + tempMin
                if self.ifOk(piles, H, tempMid):
                    tempMax = tempMid
                else:
                    tempMin = tempMid + 1
            return tempMin

    def ifOk(self, piles, H, K):
        hourNeed = 0
        for pile in piles:
            if pile % K == 0:
                hourNeed = hourNeed + pile // K
            else:
                hourNeed = hourNeed + pile // K + 1
            if hourNeed > H:
                return False
        return True
