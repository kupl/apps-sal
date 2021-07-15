class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        # determine right sorted subarray
        r = len(arr) - 1 
        while r >0 and arr[r] >= arr[r-1]:
            r -= 1
           
        # determine left sorted subarray that can be merged with right
        ret = r # set ret to worst case, remove all left 
        l = 0
        for l in range(len(arr)):
            # if left subarry is not in order anymore, stop, can't do better
            if l>0 and arr[l] < arr[l-1]:
                break
            # if l==r
            if l == r:
                return 0
                
            while r < len(arr) and arr[l] > arr[r] :
                r +=1
            

            ret = min(ret, r-l-1)
                
            
            
        return ret
            

        

        

        
        

