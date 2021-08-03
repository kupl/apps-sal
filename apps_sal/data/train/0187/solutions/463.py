class Solution:
    def minOperationsMaxProfit(self, customers: List[int], b_cost: int, r_cost: int) -> int:
        A = customers
        # cc, 3 0, four 0s. 累积的wating！=0，但是cur=0
        profit = 0
        times = 0
        cotinues_0 = 0
        waiting = 0
        max_profit = 0
        best_times = 0
        out = []
        pass_customer = 0
        for cur in A:
            waiting += cur
            # if waiting == 0:
            #     cotinues_0 += 1
            #     # if continues_0 > 3: 可能不需要
            #     #     # no charge
            #     #     pass
            #     # else:
            #     # profit -= r_cost
            #     # times += 1
            # else:
            cotinues_0 = 0
            if waiting >= 4:
                pass_customer += 4
                waiting -= 4
                profit += 4 * b_cost - r_cost
            else:
                pass_customer += waiting
                profit += waiting * b_cost - r_cost
                waiting = 0
            times += 1
            # print(times, waiting)
            if max_profit < profit:
                best_times = times
                max_profit = profit

        # print(max_profit, times, pass_customer, waiting)

        remain = waiting // 4
        profit += 4 * b_cost - r_cost
        times += remain
        if waiting % 4 != 0:
            # print(\"final cost=\" + str((waiting% 4) * b_cost - r_cost))
            if (waiting % 4) * b_cost - r_cost > 0:
                # print(\"add 1\")
                times += 1
                profit += (waiting % 4) * b_cost - r_cost
        if max_profit < profit:
            out.insert(0, (max_profit, times))
            best_times = times
            max_profit = profit
        # print(out)
        # print(sum(A), len(A), \"remain=\"+str(remain))
        return best_times if max_profit > 0 else -1
