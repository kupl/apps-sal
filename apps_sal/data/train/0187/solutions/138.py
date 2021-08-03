class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        answer = 0
        current = 0
        counter = 0
        result = -1
        for entry in customers:
            counter += 1
            wait += entry
            current -= runningCost
            if wait >= 4:
                current += (4 * boardingCost)
                wait -= 4
            else:
                current += (wait * boardingCost)
                wait = 0
            if current > answer:
                result = counter
            answer = max(answer, current)
        while wait > 0:
            counter += 1
            current -= runningCost
            if wait >= 4:
                current += (4 * boardingCost)
                wait -= 4
            else:
                current += (wait * boardingCost)
                wait = 0
            if current > answer:
                result = counter
            answer = max(answer, current)
        return result
