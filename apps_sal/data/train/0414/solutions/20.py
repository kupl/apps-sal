class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        j = 1
        
        c = k
        
        while c > 0 and j <len(arr):
            if arr[i] > arr[j]:
                j += 1
                c -= 1
            else:
                i = j 
                j += 1
                c = k -1
        return arr[i] 

