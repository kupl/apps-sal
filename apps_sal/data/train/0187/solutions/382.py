class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i = 0
        r = 0
        revn = 0
        cost = 0
        no = 0
        maxp = 0
        while i < len(customers) or r > 0:
            if i < len(customers):
                r += customers[i]
                i += 1
            cost += runningCost
            p = min(4, r)
            revn += p * boardingCost
            r -= p
            no += 1
            if revn - cost > maxp:
                maxp = revn - cost
                ans = no
        # print(revn, cost)
        return ans if revn > cost else -1
