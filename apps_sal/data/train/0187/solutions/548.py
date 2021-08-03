class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        _max = float('-inf')
        queue, index, profit, rotations, buffer = 0, 0, 0, 0, 0
        _len = len(customers)
        while queue >= 0 and index < _len:
            queue += customers[index]
            profit += ((min(queue, 4) * boardingCost) - (runningCost))
            queue -= min(queue, 4)
            if profit > _max:
                rotations += 1
            if profit == _max:
                buffer += 1
            _max = max(_max, profit)
            index += 1
            if index == _len and queue:
                profit += ((((queue // 4) * 4) * boardingCost) - ((queue // 4) * runningCost))
                _max = max(_max, profit)
                rotations += queue // 4
                queue -= ((queue // 4) * 4)

        if queue:
            profit += ((queue % 4 * boardingCost) - runningCost)
            if profit > _max:
                rotations += 1
            _max = max(_max, profit)

        return rotations + buffer if _max >= 0 else -1
