class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # dp = [{}] * n # This is incorrect. It makes just one dictionary object, not n of them.
        dp = [{} for _ in range(n)]
        result = 2
        
        for i in range(1, n):
            for j in range(i):
                delta = nums[i] - nums[j]
                longestArithSeq = 2
                
                # If we're adding on to the longest arithmetic sequence seen thus far.
                if delta in dp[j]:
                    longestArithSeq = dp[j].get(delta) + 1
                    
                # Add it to the dictionary.
                dp[i][delta] = longestArithSeq
                
                # Update the result.
                result = max(result, longestArithSeq)
                
                if result == 3:
                    print('dim')
        
        return result
