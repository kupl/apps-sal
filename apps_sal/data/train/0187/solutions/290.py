class Solution:
    def minOperationsMaxProfit(self, customers: List[int], board: int, run: int) -> int:
        if board * 4 <= run:
            return -1

        cur_prof = 0
        max_prof = 0
        waiting = 0
        res = 0
        i = 0
        while waiting > 0 or i < len(customers):
            c = 0 if i >= len(customers) else customers[i]
            serv = min(waiting + c, 4)
            waiting = waiting + c - serv

            cur_prof += board * serv - run
            if max_prof < cur_prof:
                max_prof = cur_prof
                res = i + 1
            i += 1

        if max_prof == 0:
            return -1
        return res
