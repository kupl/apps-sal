class Solution:
    def profit(self, s, customers, count, curr_profit, waiting, rot_cost, bill):
        # print(s,waiting,count)
        if curr_profit > self.profit_so_far:
            self.profit_so_far = curr_profit
            self.ans = count

        if waiting == 0 and s >= len(customers):
            return
        if s >= len(customers) and waiting > 4:
            n = waiting // 4
            waiting = waiting - (n * 4)
            count += (n)

            curr_profit += (n * 4 * bill - (n) * rot_cost)

            self.profit(len(customers), customers, count, curr_profit, waiting, rot_cost, bill)
            return

        if s < len(customers):
            waiting += customers[s]
        curr_profit -= rot_cost
        if waiting <= 4:

            curr_profit += waiting * bill
            waiting = 0
        else:
            waiting -= 4
            curr_profit += 4 * bill
        self.profit(s + 1, customers, count + 1, curr_profit, waiting, rot_cost, bill)

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        self.ans = -1
        self.profit_so_far = 0
        self.profit(0, customers, 0, 0, 0, runningCost, boardingCost)
        return self.ans
