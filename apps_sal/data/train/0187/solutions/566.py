class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 < runningCost:
            return -1
        rot = 0
        spot = 0
        prof = max_prof = [0, 0]
        while spot < len(customers):
            rot += 1
            curr = customers[spot]
            if curr > 4:
                if spot == len(customers) - 1:
                    temp = prof[0] + 4 * boardingCost * (curr // 4) - runningCost * (curr // 4)
                    max_prof1 = max(max_prof, [temp, rot - 1 + curr // 4])
                    temp = prof[0] + 4 * boardingCost * (curr // 4) + boardingCost * (curr % 4) - runningCost * (curr // 4 + bool(curr % 4))
                    max_prof2 = max(max_prof, [temp, rot - 1 + curr // 4 + bool(curr % 4)])
                    if max_prof1[0] != max_prof2[0]:
                        return max(max_prof1, max_prof2)[1]
                    if max_prof1[0] == max_prof2[0]:
                        return max_prof1[1]
                else:
                    customers[spot + 1] += curr - 4
                prof[0] += 4 * boardingCost - runningCost
            else:
                prof[0] += curr * boardingCost - runningCost
            max_prof = max(max_prof, [prof[0], rot])
            spot += 1
        return max_prof[1]
