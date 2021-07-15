class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = 0
        q = 0
        ans = -float('inf')
        for i,c in enumerate(customers,1):
            q += c
            if q <= 4:
                cur += boardingCost*q - runningCost
                q = 0
            else:
                q -= 4
                cur += boardingCost*4 - runningCost
            if ans < cur:
                ans = cur
                cnt = i
        while q:
            i += 1
            if q <= 4:
                cur += boardingCost*q - runningCost
                q = 0
            else:
                q -= 4
                cur += boardingCost*4 - runningCost
            if ans < cur:
                ans = cur
                cnt = i
        if ans > 0:
            return cnt
        else:
            return -1

            

