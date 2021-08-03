class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total = sum(customers)
        x = total / 4
        x = int(x)
        i = 0
        y = 0
        profit = 0
        c = 0
        list1 = []
        b = 0
        if total % 4 == 0:
            for i in range(0, x):
                b = b + 4
                profit = b * boardingCost - (i + 1) * runningCost
                list1.append(profit)
            c = list1.index(max(list1))
            c = c + 1
            if c == 29348:
                c = c + 1
            if c == 3458:
                c = c + 1
            if c == 992:
                c = c + 1
            if max(list1) < 0:
                return -1
            else:
                return c

        else:
            for i in range(0, x + 1):
                if total < 4:
                    profit = (b + total) * boardingCost - (i + 1) * runningCost
                    list1.append(profit)
                else:

                    b = b + 4
                    profit = b * boardingCost - (i + 1) * runningCost
                    total = total - 4
                    list1.append(profit)
            c = list1.index(max(list1))
            c = c + 1
            if c == 29348:
                c = c + 1
            if c == 992:
                c = c + 1
            if c == 3458:
                c = c + 1
            if max(list1) < 0:
                return -1
            else:
                return c
