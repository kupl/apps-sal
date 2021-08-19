class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        r = 0
        c = 0
        n = len(customers)
        total = 0
        ans = 0
        ind = -1
        while c < n:
            if customers[c] >= 4:
                r += customers[c] // 4
                total += customers[c] // 4 * 4
                customers[c] -= customers[c] // 4 * 4
                if customers[c] == 0:
                    c += 1
                res = total * boardingCost - r * runningCost
                if res > ans:
                    ans = res
                    ind = r
            else:
                if c == n - 1 or c == r:
                    total += customers[c]
                    r += 1
                    res = total * boardingCost - r * runningCost
                    if res > ans:
                        ans = res
                        ind = r
                else:
                    customers[c + 1] += customers[c]
                c += 1
        return ind
