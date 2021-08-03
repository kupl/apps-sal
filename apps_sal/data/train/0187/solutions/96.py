class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rem, rot, best_rots = 0, 1, 0
        wheel, max_benefit = 0, 0

        for cust in customers:
            total_people = (cust + rem)
            if total_people > 4:
                rem = (total_people - 4)
                wheel += 4
            else:
                wheel += total_people
                rem = 0

            if (wheel * boardingCost) - (rot * runningCost) > max_benefit:
                max_benefit = (wheel * boardingCost) - (rot * runningCost)
                best_rots = rot

            rot += 1

        while rem != 0:
            if rem > 4:
                wheel += 4
                rem -= 4
            else:
                wheel += rem
                rem = 0

            if (wheel * boardingCost) - (rot * runningCost) > max_benefit:
                max_benefit = (wheel * boardingCost) - (rot * runningCost)
                best_rots = rot

            rot += 1

        return best_rots if max_benefit > 0 else -1
