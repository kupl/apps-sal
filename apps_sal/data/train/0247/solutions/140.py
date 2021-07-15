class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        s = 0
        j = 0
        ans = float('inf')
        res = [float('inf')] * len(arr)
        currMin = float('inf')
        for i in range(len(arr)):
            
            s += arr[i]
            while s > target:
                s -= arr[j]
                j += 1
            if s == target:
                
                
                currMin = min(currMin, i - j + 1)
                ans = min(ans, res[j-1] + i - j + 1)
            
            res[i] = currMin
            
        
        return ans if ans < float('inf') else -1
            
            
            

