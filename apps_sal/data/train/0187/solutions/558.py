class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cs = [customers[0]]
        for tmp in customers[1:]:
            cs.append(cs[-1] + tmp)
        maxp = -1
        maxn = -1
        max_cap = 0
        for i in range(len(customers)):
            max_cap = min(cs[i], max_cap + 4)
            cur_profit = max_cap * boardingCost - runningCost * (i + 1)
            if cur_profit > maxp:
                maxp = cur_profit
                maxn = i + 1
        ppl_left = cs[-1] - max_cap
        rounds = ppl_left // 4
        cur_profit += rounds * (4 * boardingCost - runningCost)
        cur_round = len(customers) + rounds
        if cur_profit > maxp:
            maxp = cur_profit
            maxn = cur_round
        ppl_left2 = ppl_left % 4
        cur_profit += (ppl_left2 * boardingCost - runningCost)
        cur_round += 1
        if cur_profit > maxp:
            maxp = cur_profit
            maxn = cur_round

        return maxn
