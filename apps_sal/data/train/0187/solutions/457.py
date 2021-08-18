class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        def oneRound(waiting, max_prof, max_prof_ind, curr_prof, ind, arr):
            waiting += arr
            on_cart = waiting if waiting < 4 else 4
            waiting -= on_cart
            curr_prof = curr_prof + on_cart * boardingCost - runningCost
            if curr_prof > max_prof:
                max_prof = curr_prof
                max_prof_ind = ind + 1

            return (waiting, max_prof, max_prof_ind, curr_prof)

        waiting = 0
        max_prof = 0
        max_prof_ind = -1
        curr_prof = 0

        for ind, arr in enumerate(customers):
            (waiting, max_prof, max_prof_ind, curr_prof) = oneRound(waiting, max_prof, max_prof_ind, curr_prof, ind, arr)
        while(waiting > 0):
            ind += 1
            arr = 0
            (waiting, max_prof, max_prof_ind, curr_prof) = oneRound(waiting, max_prof, max_prof_ind, curr_prof, ind, arr)

        return max_prof_ind
