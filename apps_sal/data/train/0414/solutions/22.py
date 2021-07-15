class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        n =len(arr)
        winner = max(arr[0] , arr[1])
        if k == 1 : 
            return winner 
        
        ctn = 1
        maxNum = winner
        
        for i in range(2,n ):
            tmp = arr[i]
            if  winner > tmp :
                ctn +=1 
            
            else : 
                ctn = 1 
                winner = tmp
            
            if ctn == k : 
                return winner 
            
            maxNum = max(maxNum, tmp)
        return maxNum 
                

