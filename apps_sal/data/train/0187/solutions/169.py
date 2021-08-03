class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        d = {}
        rotations, sum_cust = 0, 0
        d[0] = 0

        for i, current in enumerate(customers):
            sum_cust += current

            if sum_cust >= 4:
                while sum_cust >= 4:
                    rotations += 1
                    d[rotations] = d[rotations - 1] + 4 * boardingCost - runningCost
                    sum_cust -= 4
            else:
                if i + 1 in d:
                    continue
                rotations += 1
                d[rotations] = d[rotations - 1] + sum_cust * boardingCost - runningCost
                sum_cust = 0

        if sum_cust > 0:
            rotations += 1
            d[rotations] = d[rotations - 1] + sum_cust * boardingCost - runningCost
            sum_cust = 0

        # print(d)
        d[0] = -1
        tmp, res = -1, -1
        for i in d:
            if tmp < d[i]:
                tmp = d[i]
                res = i
        return res
