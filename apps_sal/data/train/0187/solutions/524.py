class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boarding_cost: int, running_cost: int) -> int:
        max_profit = -1
        cur_profit = 0
        waiting = 0
        rotations = 0
        i = 0
        while i < len(customers):

            c = customers[i]
            waiting += c
            boarded = min([waiting,4])
            waiting = max([waiting-boarded,0])
            cur_profit += boarded * boarding_cost - running_cost
            if cur_profit > 0 and max_profit < cur_profit:
                max_profit = max([max_profit,cur_profit])
                rotations = i+1
            i+=1
        while waiting >0:
            boarded = min([waiting,4])
            waiting = max([waiting-boarded,0])
            cur_profit += boarded * boarding_cost - running_cost
            if cur_profit > 0 and max_profit < cur_profit:
                max_profit = max([max_profit,cur_profit])
                rotations = i+1
            i+=1
        if rotations == 0:
            return -1
        return rotations
