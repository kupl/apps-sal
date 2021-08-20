import numpy as np


class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        direc = np.zeros((len(profit), 2))
        direc[:, 0] = difficulty
        direc[:, 1] = profit
        direc = direc[direc[:, 0].argsort()]
        max_profit = np.array(direc[:, 1])
        for i in range(1, len(profit)):
            if max_profit[i - 1] > direc[i, 1]:
                max_profit[i] = max_profit[i - 1]
        result = 0
        for j in range(len(worker)):
            ind = np.searchsorted(direc[:, 0], worker[j], side='Right') - 1
            if ind > -1:
                result += max_profit[ind]
        return int(result)
