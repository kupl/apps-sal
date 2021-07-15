import numpy as np
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        direc = np.zeros((len(profit),2))
        direc[:,0] = difficulty
        direc[:,1] = profit
        direc = direc[direc[:,0].argsort()]
        # print(direc)
        max_profit = np.array(direc[:,1])
        for i in range(1,len(profit)):
            if max_profit[i-1] > direc[i,1]:
                max_profit[i] = max_profit[i-1]
        # print(max_profit)
        result = 0
        for j in range(len(worker)):
            # if worker[j] in difficulty:
            #     ind = np.searchsorted(direc[:,0],worker[j],side = 'Left')
            # else: ind = np.searchsorted(direc[:,0],worker[j],side = 'Left') - 1
            ind = np.searchsorted(direc[:,0],worker[j],side = 'Right') - 1
            # print(ind,max_profit[ind])
            if ind >-1:result += max_profit[ind]
        return int(result)
