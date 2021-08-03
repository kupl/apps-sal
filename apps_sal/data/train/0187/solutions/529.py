class Solution:
    def minOperationsMaxProfit(self, a: List[int], boardingCost: int, runningCost: int) -> int:
        res = boarding = profit = rem = 0
        n = len(a)
        cap = 4
        profits = []

        i = 0
        while rem or i < n:
            if i < n:
                rem += a[i]
                # print(f'{rem = }')
            boarding = min(rem, cap)
            # print(f'{boarding = }')
            rem = max(0, rem - cap)
            profit += boarding * boardingCost - runningCost
            profits.append(profit)
            # print(f'{rem = }')
            # print(f'{profits = }')
            i += 1

        argmax = -1
        mx = -float('inf')
        for i, x in enumerate(profits):
            if x > mx:
                mx = x
                argmax = i

        return argmax + 1 if profits[argmax] > 0 else -1
