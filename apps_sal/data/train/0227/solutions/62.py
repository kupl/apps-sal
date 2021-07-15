class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        windowstart, curr0,res = 0,0, 0
        currwindow = {1:0 , 0:0}
        
        
        for windowend in range(len(A)):

        # add the new element into the current window,
                currwindow[A[windowend]] +=1
        # check if the least common number is above k
                curr0 = currwindow[0]

        # if yes, increase the window start 
                if curr0 > K :
                        currwindow[A[windowstart]] -=1
                        windowstart +=1
                        
        # look for the window size and max with the max and the current length
                res = max (res, windowend-windowstart +1 )

        return res 
