import copy
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        arrLen = len(arr)
        if(arrLen <= k):
            arr.sort()
            return arr[-1]
        
        targ = 0
        i1 = 0
        i2 = 1
        
        while(targ < k) and arrLen > i2:
            if(arr[i1] > arr[i2]):
                i2 += 1
            else:
                i1 = i2
                i2 += 1
                targ = 0
                
            targ += 1
            
        return arr[i1]
