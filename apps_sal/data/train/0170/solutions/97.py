class Solution:
    # O(n)
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        # determine right sorted subarray
        r = len(arr) - 1 
        while r >0 and arr[r] >= arr[r-1]:
            r -= 1
        
        # r == 0 means array is sorted
        if r == 0:
            return 0
        
        # now determine left sorted subarray that can be merged with right
        ret = r # set ret to worst case, remove all left 
        l = 0
        for l in range(len(arr)):
            # if left subarry is not in order anymore, stop, can't do better
            if l>0 and arr[l] < arr[l-1]:
                break
            
            # if arr[l] is larger than the left edge of right sorted subarray, 
            # push the edge to the right
            # why this work? Is it OK to push to the right? We won't consider
            # arr[i+1] and arr[r].
            # It's OK! We don't have to consider arr[i+1] and arr[r].
            # if arr[i] is larger than the left edge, arr[next i] is larger too!
            # so it won't be the possible answer
            while r < len(arr) and arr[l] > arr[r] :
                r +=1

            ret = min(ret, r-l-1)

        return ret
            

        

        

        
        

