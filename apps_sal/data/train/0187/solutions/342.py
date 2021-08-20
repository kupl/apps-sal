class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        arr = [-1]
        currentCost = 0
        maximum = -1000000000
        rotations = 0
        total = 0
        while total != 0 or rotations < len(customers):
            if rotations < len(customers):
                total += customers[rotations]
            if total < 4:
                temp = total
                total = 0
                currentCost += temp * boardingCost - runningCost
                arr.append(currentCost)
                if currentCost > maximum:
                    maximum = currentCost
            else:
                total -= 4
                currentCost += 4 * boardingCost - runningCost
                arr.append(currentCost)
            rotations += 1
        maxer = -1000000000
        indexer = -1
        for i in range(len(arr)):
            if maxer < arr[i]:
                maxer = arr[i]
                indexer = i
        if indexer == 0:
            return -1
        return indexer
