class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        ans = -1
        rotate = 1
        current = 0
        rotate_times = -1
        for i, number in enumerate(customers):
            if number > 4:
                res += number - 4
                current += 4
            elif number == 4:
                current += number
            else:
                if res + number > 4:
                    current += 4
                    res = res + number - 4
                else:
                    current += res + number
                    res = 0
            profit = boardingCost * current - rotate * runningCost
            rotate += 1
            if ans < profit:
                ans = profit
                rotate_times = rotate

        while res > 0:
            if res > 4:
                current += 4
                res -= 4
            else:
                current += res
                res = 0
            profit = boardingCost * current - rotate * runningCost
            rotate += 1
            if ans < profit:
                ans = profit
                rotate_times = rotate
        return rotate_times - 1 if rotate_times - 1 > 0 else -1
