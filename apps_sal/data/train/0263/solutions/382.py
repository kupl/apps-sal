import numpy as np
class Solution:
    def knightDialer(self, n: int) -> int:
        ans = np.ones((10,),dtype=int)
        table = {0:[4,6],
                 1:[6,8],
                 2:[7,9],
                 3:[4,8],
                 4:[0,3,9],
                 6:[0,1,7],
                 7:[2,6],
                 8:[1,3],
                 9:[4,2]
                }
   
        for i in range(n-1):
            tempans = np.zeros((10,),dtype=int)
            for j in range(10):
                if j!=5:
                    values = table.get(j)
                    for value in values:
                        tempans[value] += ans[j]
            ans = tempans
            if(sum(ans)>10**9+7):
                ans = ans%(10**9+7)
        return sum(ans)%(10**9+7)
                            
                    

