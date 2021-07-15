class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {} #stores the longest len of arithmetic subsequence for each pair of (idx, diff)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1 
        return max(dp.values())
    
    #for A[i] and A[j], we store by ith idx and their diff the length of subsequence that follows diff A[j]-A[i]. Next time when cur A[j] becomes the first num and we find another item in A that's A[j]-A[i] away from cur A[j], we increment this subsequence's length by 1

