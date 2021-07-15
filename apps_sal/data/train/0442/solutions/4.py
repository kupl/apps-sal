class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        maxRight = [0]* len(grid)
        
        for i in range(len(grid)):
            j = len(grid[i]) - 1
            while j >= 0 and grid[i][j] != 1:
                j -= 1
            maxRight[i] = j
            
       
            
        swaps = 0
        for i in range(len(maxRight)):
            if maxRight[i] > i:
                j = i
                while j < len(maxRight) and maxRight[j] > i:
                    j += 1
                    
                if j == len(maxRight):
                    return -1
                
                while j != i:
                    temp = maxRight[j]
                    maxRight[j] = maxRight[j-1]
                    maxRight[j-1] = temp
                    swaps += 1
                    j -= 1
            

        return swaps
            
                
            
            
            

