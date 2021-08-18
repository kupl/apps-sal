class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = (0, -1)
        board = 0
        for i in range(len(customers) - 1):
            curadd = min(4, customers[i])
            board += curadd
            bc = board * boardingCost
            rc = (i + 1) * runningCost
            curpr = bc - rc
            if curpr > ans[0]:
                ans = (curpr, i + 1)
            diff = max(customers[i] - curadd, 0)
            if diff > 0:
                customers[i + 1] += diff

        remaining = customers[-1]
        i = len(customers)

        while remaining > 0:
            board += min(4, remaining)
            bc = board * boardingCost
            rc = i * runningCost
            curpr = bc - rc
            if curpr > ans[0]:
                ans = (curpr, i)
            remaining = max(remaining - 4, 0)
            i += 1

        return ans[1] if ans[0] > 0 else -1
