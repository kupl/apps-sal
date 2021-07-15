class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        
        dp = [{0: 1}]
        
        max_val = 1
        
        for i in range(1, len(A)):
            dp.append({0: 1})
            
            i_val = A[i]
            last_map = dp[-1]
            
            for j in range(i):
                j_val = A[j]
                diff = i_val - j_val
                
                diff_val = 2
                
                if diff in dp[j]:
                    diff_val = dp[j][diff] + 1
                
                if diff not in last_map:
                    last_map[diff] = diff_val
                else:
                    last_map[diff] = max(last_map[diff], diff_val)
                
                max_val = max(max_val, diff_val)
                    
        return max_val
            
                
                
        
        # every sequence is trivially 1 for itself.
        
        
        # start at index 1
        
            # loop up to this index
                # get the difference of i and j
                    
                    # have we seen that difference before? if so, add a 1 to that amount.
                    # if we have, take the max of the two times we've seen differences
        
        
        # return the max difference we've seen so far.

