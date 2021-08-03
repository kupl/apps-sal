import math


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total_people = 0
        comp_people = 0
        waitlist = 0
        rotates = 0
        gondola_size = 4
        current_profit = [-1]
        for customer in customers:
            total_people += customer
            if customer > gondola_size or waitlist > gondola_size:
                waitlist = waitlist + (customer - gondola_size)
                comp_people += gondola_size
            else:
                comp_people += customer

            rotates += 1
            current_profit.append((comp_people * boardingCost) - (rotates * runningCost))

        #rotates+= math.ceil(waitlist/gondola_size)
        #print(total_people, comp_people, waitlist, rotates, current_profit)
        while waitlist > 0:

            rotates += 1
            if waitlist > 4:
                waitlist -= gondola_size
                comp_people += gondola_size
            else:
                comp_people += waitlist
                waitlist = 0

            current_profit.append((comp_people * boardingCost) - (rotates * runningCost))

        #print(total_people, comp_people, waitlist, rotates, current_profit )
        res = current_profit.index(max(current_profit))
        if res == 0:
            return -1
        else:
            return res
