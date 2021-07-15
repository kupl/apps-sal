class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        res = [float('inf')] * len(arr)
        ans = float('inf')
        currMin = float('inf')
        i = 0
        s = 0
        for j in range(len(arr)):
            s += arr[j]
            while s > target:
                s -= arr[i]
                i += 1
            if s == target:
                currMin = min(currMin, j - i + 1)
                ans = min(ans, j - i + 1 + res[i-1])
                
            res[j] = currMin
            
        return ans if ans < float('inf') else -1

