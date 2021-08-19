class Solution:

    def minOperationsMaxProfit(self, customers: List[int], bCost: int, rCost: int) -> int:
        maxProfit = -1
        unboard = 1
        board = 0
        flag = True
        count = 0
        profit = 0
        ans = 0
        while unboard > 0 or count < len(customers):
            if flag:
                unboard = 0
                flag = False
            unboard += customers[count] if count < len(customers) else 0
            count += 1
            if unboard > 4:
                board += 4
                unboard -= 4
                profit = board * bCost - rCost * count
            else:
                board += unboard
                unboard = 0
                profit = board * bCost - rCost * count
            ans = count if profit > maxProfit else ans
            maxProfit = profit if profit > maxProfit else maxProfit
        return ans if maxProfit > 0 else -1
