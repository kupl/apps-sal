import bisect
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        start = None
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                start = i
                break
                
        if start == None:
            return 0 
        
        for i in range(len(arr)-1, 0, -1):
            if arr[i] < arr[i-1]:
                end = i
                break

        best_dist = end
        for i in range(start, -1, -1):
            j = bisect.bisect_left(arr, arr[i], end, len(arr))
            dist = j - i - 1
            best_dist = min(best_dist, dist)
            
        return best_dist            


