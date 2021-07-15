class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_rot = 0
        cur_pro = 0
        max_pro = 0
        cur_wait = 0
        i = 0
        while i < len(customers):
            customer = customers[i]
            i += 1
            cur_wait += customer
            if cur_wait >= 4:
                cur_pro += 4 * boardingCost - runningCost
                cur_wait -= 4
            else:
                cur_pro += cur_wait * boardingCost - runningCost
                cur_wait = 0
            if cur_pro > max_pro:
                max_rot, max_pro = i, cur_pro
        
        while cur_wait > 0:
            i += 1
            if cur_wait >= 4:
                cur_pro += 4 * boardingCost - runningCost
                cur_wait -= 4
            else:
                cur_pro += cur_wait * boardingCost - runningCost
                cur_wait = 0
            if cur_pro > max_pro:
                max_rot, max_pro = i, cur_pro
        
        return max_rot if max_pro > 0 else -1
