class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        from math import ceil
        n = 0
        cost = 0
        num = 0
        shift = 1
        arr = {}
        for i in customers:
            n += i
            x = min(4, n)
            num += x
            cost = (num * boardingCost) - (shift * runningCost)
            n -= min(4, n)
            if cost not in arr:
                arr[cost] = shift
            shift += 1
        while n > 0:
            x = min(4, n)
            num += x
            cost = (num * boardingCost) - (shift * runningCost)
            n -= min(4, n)
            if cost not in arr:
                arr[cost] = shift
            shift += 1
        cost = max(arr.keys())
        if cost <= 0:
            return -1
        return (arr[cost])
