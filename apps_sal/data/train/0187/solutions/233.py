class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int):
        if 4 * boardingCost < runningCost:
            return -1
        n = len(customers)
        (maxtotal, maxrotations) = (0, -1)
        (total, rotations) = (0, 1)
        i = 0
        while i != n - 1 or customers[n - 1] != 0:
            if customers[i] > 4:
                total += boardingCost * 4 - runningCost
                if i < n - 1:
                    customers[i + 1] += customers[i] - 4
                    customers[i] = 0
                else:
                    customers[i] -= 4
            else:
                total += customers[i] * boardingCost - runningCost
                customers[i] = 0
            if total > maxtotal:
                maxtotal = total
                maxrotations = rotations
            if i < n - 1:
                i += 1
            rotations += 1
        return maxrotations
