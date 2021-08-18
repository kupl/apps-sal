class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 0
        j = 0
        wait = 0
        n = len(customers)
        rot = 1
        tot = 0
        curr_max = 0
        curr_rot = 0
        while wait > 0 or j < n:
            if j < n:
                wait = wait + customers[j]
            if wait >= 4:
                wait -= 4
                tot += 4

            else:
                tot += wait
                wait = 0
            calc = (tot * boardingCost) - (rot * runningCost)
            if curr_max < calc:
                curr_rot = rot
                curr_max = calc
            j += 1
            rot += 1
        if curr_rot == 0:
            return -1
        return curr_rot
