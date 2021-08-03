class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        accuArr = []
        y = 0
        for x in arr:
            y += x
            accuArr.append(y)
        bestTill = [float('inf')] * len(arr)
        bestTillNow = float('inf')
        sum2Pos = dict()
        sum2Pos[0] = -1
        res = float('inf')
        for i in range(len(accuArr)):
            currAccu = accuArr[i]
            preSum = currAccu - target
            if preSum in sum2Pos:
                preEnd = sum2Pos[preSum]
                currLength = i - preEnd

                if preEnd != -1:
                    res = min(res, currLength + bestTill[preEnd])

                bestTillNow = min(bestTillNow, currLength)

            sum2Pos[currAccu] = i
            bestTill[i] = bestTillNow

        return res if res != float('inf') else -1
