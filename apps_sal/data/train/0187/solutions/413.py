class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        q = 0

        idx = -1

        dd = collections.defaultdict(int)

        book = collections.defaultdict(int)

        profit = 0

        for i in range(len(customers)):
            q += customers[i]
            if q:
                dd[i % 4] = 1
            if q > 4:
                profit += boardingCost * 4
                q -= 4
            else:
                profit += boardingCost * q
                q = 0
            profit -= runningCost
            dd[(i - 1) % 4] = 0
            book[i] = profit

        while q:
            i += 1
            if q > 4:
                profit += boardingCost * 4
                q -= 4
            else:
                profit += boardingCost * q
                q = 0
            profit -= runningCost
            dd[i % 4] = 1
            dd[i % 4 - 1] = 0
            book[i] = profit

        maxi = max(book.values())

        if maxi < 1:
            return - 1

        for i in sorted(book.keys()):
            if book[i] == maxi:
                return i + 1
