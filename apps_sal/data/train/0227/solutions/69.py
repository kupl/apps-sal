class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        res = -1
        start, count = 0, 0 # start is beginning of window, count is number of 1s
        # i is end of window, hence len of window is i-start+1
        
        for i in range(len(A)):
            if A[i]==1: count += 1
            while (i-start+1-count > K):
                if A[start]==1: count -= 1
                start += 1
            res = max(res, i-start+1)
        
        return res
                

