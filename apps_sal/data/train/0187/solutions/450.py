class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = float('-inf')
        sofar = 0
        people = 0
        count = 0
        idx = 0
        while idx < len(customers) or people:
            if idx < len(customers):
                people += customers[idx]
            idx += 1
            earning = -runningCost
            if people > 4:
                earning += 4 * boardingCost
                people -= 4
            else:
                earning += people * boardingCost
                people = 0
            sofar += earning
            if sofar > ans:
                count = idx
            ans = max(ans, sofar)
        if ans < 0:
            return -1
        return count
