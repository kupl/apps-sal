class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        M = 10 **9 + 7
        #think all odd as 1 and even as 0 
        new_arr = [ 1 if i %2 == 1 else 0 for i in  arr]
        res = 0
        cucr_sum = 0
        cash = {0:1, 1: 0}
        for end in range(len(new_arr)):
            cucr_sum += new_arr[end]
            if cucr_sum%2 == 1:
                res += cash[0]
                cash[1] += 1
                
            else:
                res += cash[1]
                cash[0] += 1
        
        return res%M
                
            

