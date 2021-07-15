# [9,9,6,0,6,6,9]

# [1,1,-1,-1,-1,1]
#  1 2  1  0  -1 0
# [1,1,-1,-1,-1,1, 1]
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = []
        for hour in hours:
            if hour > 8:
                prefix.append(1)
            else:
                prefix.append(-1)
                
        curr_sum = 0
        seen = {0:-1}
        res = 0
        
        for i, num in enumerate(prefix):
            curr_sum += num
            if curr_sum > 0:
                res = i + 1
                
            if curr_sum - 1 in seen:
                res = max(res, i - seen[curr_sum - 1])
            
            if curr_sum not in seen:
                seen[curr_sum] = i
        
        return res
    
        

