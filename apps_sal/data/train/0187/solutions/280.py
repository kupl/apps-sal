class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_result = 0
        max_count = 0
        result = 0
        waiting = 0
        count = 0
        if boardingCost * 4 <= runningCost:
            return -1

        for i in customers:

            waiting += i
            next_board = min(waiting, 4)
            waiting -= next_board
            result += boardingCost * next_board
            count += 1
            result -= runningCost
            if result > max_result:
                max_result = result
                max_count = count


        full_batch = waiting // 4
        result += full_batch * 4 * boardingCost
        if full_batch > 0:
            result -= full_batch * runningCost
            count += full_batch


        if result > max_result:
            max_result = result
            max_count = count

        waiting -= full_batch * 4
        if waiting * boardingCost > runningCost:
            result += waiting * boardingCost - runningCost
            count += 1

        if result > max_result:
            max_result = result
            max_count = count

        return max_count
